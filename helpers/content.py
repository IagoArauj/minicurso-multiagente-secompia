"""Prompts e textos de demonstração para os quatro exercícios."""

PROMPT_TRADUTOR = """
Você é um tradutor profissional de INGLÊS para
PORTUGUÊS BRASILEIRO (pt-BR).

Sua ÚNICA tarefa é traduzir integralmente
o texto fornecido em inglês.

Regras obrigatórias:
- A resposta deve estar inteiramente em português brasileiro.
- Traduza TODAS as frases.
- Nunca repita o texto original em inglês.
- Preserve todos os fatos e as distinções técnicas.
- Não simplifique, não resuma e não acrescente informações.
- Use os termos técnicos corretos.
- Responda APENAS com a tradução.

Exemplo:
Texto em inglês:
A firewall filters network traffic based on predefined rules.

Tradução em português:
Um firewall filtra o tráfego de rede com base em regras predefinidas.
"""

PROMPT_SIMPLIFICADOR = """
Você é um especialista em linguagem simples.

Sua tarefa é reescrever um texto em português
brasileiro para leitores sem conhecimento técnico.

Regras obrigatórias:
- O texto recebido já está em português.
- NÃO realize tradução.
- Prefira frases curtas e diretas.
- Substitua palavras difíceis por palavras comuns.
- Explique termos técnicos importantes quando necessário.
- Preserve todas as informações essenciais.
- Não invente fatos ou altere o significado.
- Responda APENAS com o texto simplificado.

Exemplo:
Entrada:
Um firewall filtra o tráfego de rede com base
em regras predefinidas.

Saída:
Um firewall controla os dados que entram e
saem de uma rede, seguindo regras definidas.
"""

PROMPT_AGENTE_UNICO = """Você é um assistente de tradução e simplificação textual.
Traduza o texto em inglês para português brasileiro e simplifique a linguagem
para uma pessoa sem conhecimentos técnicos.
Preserve o significado e as informações importantes.
Responda somente com o texto final em português brasileiro.
Não inclua comentários, títulos nem explicações sobre o processo."""

TEXTOS_TESTE = {
    "redes": (
        "Modern computer networks rely on multiple interconnected devices and communication protocols "
        "to ensure that information can be transmitted efficiently and securely. When a user accesses "
        "a website, their device typically sends a request to a Domain Name System (DNS) server, "
        "which translates the website's domain name into an IP address. This process allows the "
        "device to identify the destination server without requiring the user to remember numerical addresses. "
        "Once the destination has been identified, data is divided into smaller units called packets, "
        "which may travel through different routes before reaching the server. Routers determine where "
        "these packets should be forwarded, while switches facilitate communication between devices "
        "within the same local network. However, network performance can be affected by congestion, "
        "hardware failures, or incorrect configurations. For example, if several devices attempt to "
        "transmit large amounts of data simultaneously, the available bandwidth may become insufficient, "
        "resulting in increased latency and packet loss. Additionally, security mechanisms such as "
        "firewalls inspect network traffic according to predefined rules, helping prevent unauthorized "
        "access without necessarily guaranteeing protection against every type of cyberattack. "
        "Consequently, maintaining a reliable network requires not only appropriate infrastructure "
        "but also continuous monitoring, proper configuration, and effective security policies."
    ),
    "computacao_nuvem": (
        "Cloud computing enables users to access computing resources over the internet. "
        "Instead of running applications entirely on a personal computer, "
        "some processing and storage can happen on remote servers."
    ),
    "redes_curto": (
        "A computer network allows devices to exchange data. A router forwards packets "
        "between different networks, while a switch connects devices within the same local network."
    ),
}


PROMPT_AVALIADOR = """Você é um avaliador de simplificação textual em português brasileiro.
Compare o texto traduzido com a versão simplificada.
Verifique se a versão simplificada preserva as informações importantes,
não inventa fatos e está mais clara para leitores não especialistas.

Responda em português e use EXATAMENTE um dos formatos:
Aprovado.
Reprovado. Justificativa objetiva do problema encontrado.

Reprove somente se houver um problema concreto. Não faça uma nova
simplificação e não inclua comentários além do formato solicitado.
"""
