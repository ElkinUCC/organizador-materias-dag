# AGENTS.md

## Herramientas de IA utilizadas

Durante el desarrollo del proyecto se utilizó ChatGPT como herramienta de apoyo académico y técnico para comprender conceptos relacionados con grafos dirigidos acíclicos (DAG), algoritmos de recorrido y estructuras de datos.

---

## Rol de la IA en el proyecto

La IA fue utilizada como apoyo para:

- Explicar conceptos teóricos sobre DAG, BFS, DFS y orden topológico
- Guiar paso a paso la implementación de los algoritmos
- Ayudar en la organización de la estructura del proyecto
- Generar ejemplos de código base en Python
- Proponer casos de prueba para validar el sistema
- Resolver dudas relacionadas con lógica y dependencias entre materias

---

## Tareas realizadas con apoyo de IA

### 1. Implementación de la clase DAG

Se recibió orientación para construir la estructura principal del grafo utilizando lista de adyacencia e in-degree.

Métodos implementados:

- add_node()
- add_edge()
- print_graph()

---

### 2. Ordenamiento topológico

Se implementó el algoritmo de Kahn usando BFS y cola (`deque`) para calcular un orden válido de cursado de materias.

---

### 3. Detección de ciclos

Se implementó DFS con coloreo de nodos (blanco, gris y negro) para detectar ciclos en el grafo dirigido.

---

### 4. Materias disponibles

Se desarrolló una función que determina qué materias pueden cursarse dependiendo de las asignaturas aprobadas.

---

### 5. Cálculo de niveles

Se implementó un recorrido BFS para calcular el semestre mínimo posible de cada materia.

---

## Decisiones tomadas por el estudiante

Durante el desarrollo del proyecto se tomaron las siguientes decisiones:

- Utilizar lista de adyacencia en lugar de matriz de adyacencia por eficiencia y simplicidad
- Separar la lógica del DAG en archivos independientes
- Crear casos de prueba para validar ciclos y orden topológico
- Mantener una estructura modular y organizada del proyecto

---

## Validación y correcciones realizadas

El código generado fue revisado y probado manualmente mediante diferentes escenarios:

- DAG válido sin ciclos
- Grafo con ciclo intencional
- Materias con múltiples prerrequisitos
- Validación de materias disponibles

Además, se realizaron ajustes para comprender completamente la dirección de las aristas y el funcionamiento del algoritmo de Kahn.

---

## Aprendizajes obtenidos

Durante el proyecto se fortalecieron conocimientos sobre:

- Grafos dirigidos acíclicos (DAG)
- Recorridos BFS y DFS
- Ordenamiento topológico
- Detección de ciclos
- Modelado de dependencias académicas
- Organización de proyectos en Python