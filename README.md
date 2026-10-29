# Introdução aos Sistemas Multiagentes: da IA generativa à colaboração entre agentes

Material de apoio de um minicurso introdutório sobre **agentes de IA e sistemas multiagentes**, com exemplos práticos em **Python**, **Hugging Face Transformers** e **LangGraph**, apresentado na SECompIA 2026.

Durante o minicurso, vamos construir uma aplicação que recebe um texto em inglês, traduz para português brasileiro e depois o simplifica. O objetivo não é criar um tradutor de produção, mas entender como **separar responsabilidades entre agentes, compartilhar informações e controlar fluxos de execução**.

## O que vamos construir?

O notebook evolui em quatro etapas:

1. **Agente único:** tradução e simplificação com uma única chamada ao modelo e um único prompt.
2. **Multiagente com Python puro:** dois agentes especializados — tradutor e simplificador — executados sequencialmente.
3. **Multiagente com LangGraph:** o mesmo fluxo representado como grafo, com nós, arestas e estado compartilhado.
4. **Arestas condicionais:** inclusão de um agente avaliador, que pode aprovar a simplificação ou solicitar uma revisão, respeitando um limite de tentativas.

Ao final, comparamos os **textos produzidos, a quantidade de chamadas, os tokens utilizados e o tempo de execução**. Mais agentes não significam, necessariamente, resultados melhores.

## Tecnologias

- **Google Colab** — ambiente para executar o notebook.
- **Transformers** — carregamento e inferência de modelos de linguagem.
- **SLMs** — modelos pequenos, como `LiquidAI/LFM2.5-1.2B-Instruct` e `Qwen/Qwen3-0.6B`.
- **LangGraph** — representação e execução do fluxo de agentes.

**Não é necessário contratar APIs pagas.** Os modelos são executados no ambiente do notebook. A disponibilidade de GPU no plano gratuito do Colab, porém, não é garantida.

## Estrutura esperada

```text
.
├── minicurso_multiagentes.ipynb
└── helpers/
    ├── __init__.py
    ├── content.py       # Prompts e textos de teste
    ├── inference.py     # Carregamento do modelo e inferência
    ├── reports.py       # Exibição e comparação de resultados
    └── visualize.py     # Visualização dos grafos
```

> O notebook **não cria os arquivos de `helpers`**. Eles precisam estar presentes junto ao notebook no ambiente de execução. Confira a estrutura publicada neste repositório antes de iniciar.

## Como executar no Google Colab

1. Abra o arquivo `minicurso_multiagentes.ipynb` no [Google Colab](https://colab.research.google.com/).
2. Disponibilize a pasta `helpers/` no diretório de trabalho do Colab, preservando seus arquivos.
3. Se disponível, selecione **Ambiente de execução → Alterar o tipo de ambiente de execução → T4 GPU**.
4. Execute as células **de cima para baixo**, começando pela instalação das dependências e verificação do pacote `helpers`.
5. Acompanhe a construção das quatro arquiteturas e experimente os textos de teste.

A GPU T4 é recomendada para acelerar a geração de texto; com CPU a inferência pode ser bem mais lenta. A primeira execução também pode demorar devido ao download do modelo.

**Primeira vez no Jupyter?** Cada célula pode ser executada com `Shift + Enter`. As células compartilham variáveis em memória, por isso executá-las fora de ordem pode produzir erros. Após reiniciar o ambiente, execute novamente as etapas anteriores.

## Experimentos sugeridos

- Compare o agente único com os dois agentes especializados usando o mesmo texto.
- Observe a tradução intermediária antes da simplificação.
- Altere os prompts dos agentes e avalie as diferenças nas respostas.
- Teste o agente avaliador: quando ele solicita uma revisão? Qual é o impacto no tempo e na quantidade de tokens?
- Experimente um texto mais técnico ou outro modelo pequeno.

## Observações

Este projeto tem **finalidade educacional**. Modelos pequenos podem produzir respostas incompletas, seguir instruções incorretamente ou apresentar avaliações inconsistentes. A comparação entre as arquiteturas é exploratória, não uma demonstração de superioridade de uma abordagem.
