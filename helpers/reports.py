"""Exibição e comparação, fora da lógica dos agentes."""
import pandas as pd

from IPython.display import HTML, display
from html import escape

def mostrar_resultado(estado: dict):
    def secao(titulo, conteudo):
        return f"""
        <div style="margin-bottom: 16px;">
            <strong>{titulo}</strong>
            <div style="
                white-space: pre-wrap;
                overflow-wrap: anywhere;
                word-break: normal;
                margin-top: 6px;
                line-height: 1.6;
            ">{escape(str(conteudo))}</div>
        </div>
        """

    html = secao("ORIGINAL:", estado["original"])

    if "traducao" in estado:
        html += secao("TRADUÇÃO:", estado["traducao"])

    html += secao("SIMPLIFICAÇÃO:", estado["simplificacao"])

    estatisticas = []
    for item in estado.get("estatisticas", []):
        estatisticas.append(
            f"- {item['agente']}: {item['tempo_s']:.2f}s, "
            f"{item['input_tokens']} tokens de entrada, "
            f"{item['output_tokens']} de saída"
        )

    html += secao("ESTATÍSTICAS:", "\n".join(estatisticas))

    display(HTML(f"""
        <div style="
            max-width: 100%;
            min-width: 0;
            overflow-wrap: anywhere;
            font-family: inherit;
            font-size: 14px;
        ">
            {html}
        </div>
    """))


def tabela_comparativa(resultados: dict):
    linhas = []
    for nome, resultado in resultados.items():
        stats = resultado["estatisticas"]
        linhas.append({
            "Arquitetura": nome,
            "Chamadas": len(stats),
            "Tokens entrada": sum(x["input_tokens"] for x in stats),
            "Tokens saída": sum(x["output_tokens"] for x in stats),
            "Tempo geração (s)": round(sum(x["tempo_s"] for x in stats), 2),
            "Texto final": resultado["simplificacao"],
        })
    return pd.DataFrame(linhas)

def estatisticas_do_agente(nome: str, resposta: dict) -> dict:
    return {"agente": nome, **{
        campo: resposta[campo]
        for campo in ("input_tokens", "output_tokens", "tempo_s")
    }}