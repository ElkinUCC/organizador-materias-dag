import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(dag):
    """
    Dibuja visualmente el DAG.
    """

    # Crear grafo dirigido de NetworkX
    graph = nx.DiGraph()

    # ==================================================
    # AGREGAR NODOS Y ARISTAS
    # ==================================================

    for subject in dag.graph:

        # Agregar nodo
        graph.add_node(subject)

        # Agregar conexiones
        for neighbor in dag.graph[subject]:

            graph.add_edge(subject, neighbor)

    # ==================================================
    # CONFIGURAR VISUALIZACION
    # ==================================================

    plt.figure(figsize=(12, 8))

    # Posición automática de nodos
    pos = nx.spring_layout(
        graph,
        seed=42
    )

    # Dibujar nodos
    nx.draw_networkx_nodes(
        graph,
        pos,
        node_size=3000
    )

    # Dibujar nombres
    nx.draw_networkx_labels(
        graph,
        pos,
        font_size=9
    )

    # Dibujar aristas
    nx.draw_networkx_edges(
        graph,
        pos,
        arrows=True,
        arrowsize=20
    )

    # Título
    plt.title(
        "Malla Curricular - DAG",
        fontsize=16
    )

    # Ocultar ejes
    plt.axis("off")

    # Mostrar ventana
    plt.show()