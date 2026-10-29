"""Desenho local do grafo do LangGraph usando Graphviz."""
from IPython.display import display, Image

def visualizar_grafo(grafo):
    png = grafo.get_graph().draw_mermaid_png()
    display(Image(data=png))
