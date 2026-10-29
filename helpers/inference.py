"""Infraestrutura de inferência compartilhada por todos os agentes."""
import time
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


def carregar_modelo(model_id: str, device: str | None = None):
    device = device or ("cuda" if torch.cuda.is_available() else "cpu")
    dtype = torch.float16 if device == "cuda" else torch.float32
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=dtype)
    model = model.to(device).eval()
    return model, tokenizer, device


def consultar_llm(model, tokenizer, device, system_prompt: str, user_prompt: str, max_new_tokens: int = 240) -> dict:
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    # enable_thinking só é usado no Qwen3; outros templates podem não aceitá-lo.
    template_args = {"add_generation_prompt": True, "return_tensors": "pt", "return_dict": True}
    if "qwen3" in str(getattr(tokenizer, "name_or_path", "")).lower():
        template_args["enable_thinking"] = False
    inputs = tokenizer.apply_chat_template(messages, **template_args).to(device)
    input_tokens = inputs["input_ids"].shape[-1]
    inicio = time.perf_counter()
    with torch.inference_mode():
        output = model.generate(
            **inputs, max_new_tokens=max_new_tokens, do_sample=False,
            pad_token_id=tokenizer.eos_token_id,
        )
    if device == "cuda":
        torch.cuda.synchronize()  # tempo de execução real da GPU
    duracao = time.perf_counter() - inicio
    generated_ids = output[0, input_tokens:]
    texto = tokenizer.decode(generated_ids, skip_special_tokens=True).strip()
    if "</think>" in texto:
        texto = texto.split("</think>", 1)[1].strip()
    return {
        "texto": texto,
        "input_tokens": int(input_tokens),
        "output_tokens": int(generated_ids.numel()),
        "tempo_s": duracao,
    }
