from dag import DAG

# Crear objeto DAG
dag = DAG()

# Agregar materias
dag.add_node("Programación 1")
dag.add_node("Matemáticas Discretas")
dag.add_node("Estructura de Datos")
dag.add_node("Algoritmos")

# Agregar prerrequisitos
dag.add_edge("Programación 1", "Estructura de Datos")
dag.add_edge("Matemáticas Discretas", "Estructura de Datos")
dag.add_edge("Estructura de Datos", "Algoritmos")

##prueba de ciclos
#dag.add_edge("Algoritmos", "Programación 1")

# Mostrar grafo
dag.print_graph()

# Mostrar in-degree
print("\nIN-DEGREE:\n")
print(dag.in_degree)

# Orden topológico
order = dag.topological_sort()

print("\nORDEN TOPOLOGICO:\n")
print(order)

# Detectar ciclos
print("\n¿EL GRAFO TIENE CICLOS?\n")

if dag.has_cycle():
    print("Sí hay ciclos")
else:
    print("No hay ciclos")