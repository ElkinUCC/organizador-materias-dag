# Organizador de Materias Universitarias usando DAG

## Descripción

Este proyecto implementa una aplicación basada en Grafos Dirigidos Acíclicos (DAG) para representar la malla curricular de una carrera universitaria.

Cada materia es modelada como un nodo y los prerrequisitos como aristas dirigidas. El sistema permite calcular el orden correcto para cursar materias, detectar ciclos en la malla curricular y determinar qué materias están disponibles según las asignaturas aprobadas por el estudiante.

---

## Características

- Representación de la malla curricular mediante lista de adyacencia
- Agregar materias y prerrequisitos
- Ordenamiento topológico usando el algoritmo de Kahn
- Detección de ciclos usando DFS y coloreo de nodos
- Consulta de materias disponibles
- Cálculo de niveles o semestre mínimo de cada materia
- Casos de prueba para validar el comportamiento del sistema

---

## Tecnologías utilizadas

- Python 3
- Estructuras de datos
- Grafos dirigidos acíclicos (DAG)
- BFS (Breadth First Search)
- DFS (Depth First Search)

---

## Estructura del proyecto

```text
organizador-materias-dag/
│
├── src/
│   ├── dag.py
│   ├── main.py
│   └── test_cases.py
│
├── docs/
│   ├── AGENTS.md
│   └── analisis.md
│
├── README.md
└── requirements.txt
```

---

## Algoritmos implementados

### 1. Orden Topológico (Kahn)

Permite obtener un orden válido para cursar materias respetando los prerrequisitos académicos.

### 2. Detección de ciclos (DFS)

Se utiliza DFS con coloreo de nodos (blanco, gris y negro) para identificar dependencias circulares dentro de la malla curricular.

### 3. BFS por niveles

Se calcula el semestre mínimo posible para cursar cada materia según las dependencias existentes.

---

## Cómo ejecutar el proyecto

### Ejecutar ejemplo principal

```bash
python src/main.py
```

### Ejecutar casos de prueba

```bash
python src/test_cases.py
```

---

## Ejemplo de salida

```text
ORDEN TOPOLOGICO:

['Programación 1', 'Matemáticas', 'Estructura de Datos', 'Algoritmos']
```

---

## Autor

Elkin Augusto Amador Padilla  
Universidad Cooperativa de Colombia  
Ingeniería de Software