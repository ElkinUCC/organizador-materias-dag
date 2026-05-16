# Historial de Prompts

## Proyecto
Organizador de Materias Universitarias usando DAG

Autor:
Elkin Augusto Amador Padilla

---

# Etapa 1: Comprensión del problema

## Prompt utilizado

“Estoy viendo árboles y grafos en estructura de datos pero me perdí varias clases. Necesito entender qué es un DAG y cómo puede aplicarse a materias universitarias.”

## Objetivo

Comprender los conceptos básicos antes de programar.

## Resultado

Se comprendió:
- Qué es un DAG
- Qué es un nodo y una arista
- Qué representa un prerrequisito
- Por qué un ciclo es inválido en una malla curricular

---

# Etapa 2: Diseño de la estructura

## Prompt utilizado

“Ayúdame a estructurar un proyecto en Python para representar materias universitarias usando un DAG.”

## Objetivo

Diseñar la estructura base del proyecto.

## Resultado

Se decidió usar:
- Python
- Lista de adyacencia
- Diccionario para in-degree
- Separación por módulos

---

# Etapa 3: Implementación del DAG

## Prompt utilizado

“Explícame paso a paso cómo implementar un DAG con add_node y add_edge.”

## Objetivo

Construir la estructura principal del grafo.

## Resultado

Se implementó:
- Clase DAG
- add_node()
- add_edge()
- print_graph()

---

# Etapa 4: Ordenamiento Topológico

## Prompt utilizado

“Explícame el algoritmo de Kahn y cómo aplicarlo a materias universitarias.”

## Objetivo

Implementar el orden topológico.

## Resultado

Se desarrolló:
- topological_sort()
- manejo de in-degree
- uso de cola BFS

También se entendió la importancia de la dirección correcta de las aristas.

---

# Etapa 5: Detección de ciclos

## Prompt utilizado

“¿Cómo detectar ciclos en un DAG usando DFS?”

## Objetivo

Validar que la malla curricular no tenga dependencias imposibles.

## Resultado

Se implementó:
- has_cycle()
- DFS recursivo
- coloreo de nodos

---

# Etapa 6: Materias disponibles

## Prompt utilizado

“¿Cómo calcular qué materias puede cursar un estudiante según las materias aprobadas?”

## Objetivo

Agregar funcionalidad práctica al sistema.

## Resultado

Se implementó:
- available_subjects()

---

# Etapa 7: Cálculo de niveles

## Prompt utilizado

“¿Cómo calcular el semestre mínimo de cada materia en un DAG?”

## Objetivo

Organizar las materias por niveles académicos.

## Resultado

Se implementó:
- calculate_levels()

---

# Etapa 8: Interfaz gráfica

## Prompt utilizado

“El proyecto necesita visualización gráfica. ¿Cómo puedo mostrar el DAG visualmente en Python?”

## Objetivo

Cumplir el requisito funcional de visualización.

## Resultado

Se implementó:
- visualizer.py
- uso de NetworkX
- uso de Matplotlib

---

# Etapa 9: Eliminación de nodos

## Prompt utilizado

“¿Cómo eliminar una materia y actualizar las dependencias del DAG?”

## Objetivo

Cumplir el requisito funcional de eliminar materias.

## Resultado

Se implementó:
- delete_node()

---

# Etapa 10: Camino crítico

## Prompt utilizado

“¿Cómo calcular el camino crítico o secuencia más larga de dependencias en un DAG?”

## Objetivo

Implementar el requisito de camino crítico.

## Resultado

Se implementó:
- critical_path()

Usando:
- orden topológico
- programación dinámica

---

# Reflexión Personal

Durante el desarrollo del proyecto se utilizó la IA como apoyo para comprender conceptos complejos y organizar el trabajo por etapas.

Sin embargo, fue necesario corregir varias veces:
- la dirección de las aristas,
- el manejo del in-degree,
- problemas de indentación,
- y errores de Git/GitHub.

La parte más difícil fue comprender el algoritmo de Kahn y cómo el in-degree cambia durante el recorrido.

El uso de la IA permitió acelerar el aprendizaje, pero también fue necesario entender el código para poder corregir errores y explicar el funcionamiento del proyecto.