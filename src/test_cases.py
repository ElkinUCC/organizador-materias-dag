from dag import DAG


def test_valid_dag():

    print("\n===== PRUEBA DAG VALIDO =====\n")

    dag = DAG()

    # Materias
    dag.add_edge("Programación 1", "Estructura de Datos")
    dag.add_edge("Matemáticas", "Estructura de Datos")
    dag.add_edge("Estructura de Datos", "Algoritmos")

    # Verificar ciclo
    print("¿Tiene ciclos?")
    print(dag.has_cycle())

    # Orden topológico
    print("\nOrden topológico:")
    print(dag.topological_sort())

    # Niveles
    print("\nNiveles:")
    print(dag.calculate_levels())


def test_cycle_detection():

    print("\n===== PRUEBA CON CICLO =====\n")

    dag = DAG()

    dag.add_edge("A", "B")
    dag.add_edge("B", "C")
    dag.add_edge("C", "A")

    # Detectar ciclo
    print("¿Tiene ciclos?")
    print(dag.has_cycle())

    # Orden topológico
    print("\nOrden topológico:")
    print(dag.topological_sort())


def test_available_subjects():

    print("\n===== PRUEBA MATERIAS DISPONIBLES =====\n")

    dag = DAG()

    dag.add_edge("Programación 1", "Estructura de Datos")
    dag.add_edge("Matemáticas", "Estructura de Datos")
    dag.add_edge("Estructura de Datos", "Algoritmos")

    approved = [
        "Programación 1",
        "Matemáticas"
    ]

    print("Materias aprobadas:")
    print(approved)

    print("\nMaterias disponibles:")
    print(dag.available_subjects(approved))


# Ejecutar pruebas
test_valid_dag()
test_cycle_detection()
test_available_subjects()