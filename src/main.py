from dag import DAG


def main():
    """
    Función principal del programa.
    """

    # ==================================================
    # CREAR GRAFO
    # ==================================================

    dag = DAG()

    # ==================================================
    # AGREGAR MATERIAS
    # ==================================================

    dag.add_node("Programación 1")
    dag.add_node("Matemáticas Discretas")
    dag.add_node("Estructura de Datos")
    dag.add_node("Algoritmos")

    # ==================================================
    # AGREGAR PRERREQUISITOS
    # ==================================================

    dag.add_edge(
        "Programación 1",
        "Estructura de Datos"
    )

    dag.add_edge(
        "Matemáticas Discretas",
        "Estructura de Datos"
    )

    dag.add_edge(
        "Estructura de Datos",
        "Algoritmos"
    )

    # ==================================================
    # PRUEBA DE CICLO
    # ==================================================

    # Descomentar para probar ciclos

    # dag.add_edge(
    #     "Algoritmos",
    #     "Programación 1"
    # )

    # ==================================================
    # MOSTRAR GRAFO
    # ==================================================

    dag.print_graph()

    # ==================================================
    # MOSTRAR IN-DEGREE
    # ==================================================

    print("\nIN-DEGREE:\n")
    print(dag.in_degree)

    # ==================================================
    # ORDEN TOPOLOGICO
    # ==================================================

    order = dag.topological_sort()

    print("\nORDEN TOPOLOGICO:\n")
    print(order)

    # ==================================================
    # DETECTAR CICLOS
    # ==================================================

    print("\n¿EL GRAFO TIENE CICLOS?\n")

    if dag.has_cycle():
        print("Sí hay ciclos")
    else:
        print("No hay ciclos")

    # ==================================================
    # MATERIAS APROBADAS
    # ==================================================

    approved = [
        "Programación 1",
        "Matemáticas Discretas",
        "Estructura de Datos"
    ]

    # ==================================================
    # MATERIAS DISPONIBLES
    # ==================================================

    available = dag.available_subjects(approved)

    print("\nMATERIAS DISPONIBLES:\n")
    print(available)

    # ==================================================
    # CALCULAR NIVELES
    # ==================================================

    levels = dag.calculate_levels()

    print("\nNIVELES DE LAS MATERIAS:\n")

    for subject, level in levels.items():
        print(f"{subject}: Semestre {level}")


# ======================================================
# EJECUCION PRINCIPAL
# ======================================================

if __name__ == "__main__":
    main()