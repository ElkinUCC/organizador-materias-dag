# Documento de Análisis

# 1. Definición del Problema

El proyecto busca resolver la dificultad que tienen los estudiantes universitarios para comprender el orden correcto en el que deben cursar las materias de una carrera. Muchas asignaturas poseen prerrequisitos y dependencias que pueden generar confusión al momento de planificar los semestres académicos.

La aplicación desarrollada representa la malla curricular mediante un Grafo Dirigido Acíclico (DAG), donde cada materia corresponde a un nodo y cada prerrequisito a una arista dirigida.

El sistema permite visualizar dependencias, calcular un orden topológico de cursado, detectar ciclos o errores en la malla curricular y determinar qué materias se encuentran disponibles según las asignaturas aprobadas por el estudiante.

---

## 1.1 Usuarios del sistema

Los principales usuarios de la aplicación son:

- Estudiantes universitarios
- Coordinadores académicos
- Docentes interesados en validar estructuras curriculares

---

## 1.2 Impacto del problema

La incorrecta planificación de materias puede generar retrasos académicos, confusión en la organización semestral y errores en el cumplimiento de prerrequisitos.

Además, una malla curricular con dependencias circulares podría impedir que ciertas materias puedan cursarse correctamente.

---

## 1.3 Solución propuesta

La solución consiste en implementar una aplicación basada en DAG que permita modelar las relaciones entre materias y prerrequisitos.

El sistema utiliza algoritmos de grafos para:

- Detectar ciclos
- Calcular órdenes topológicos válidos
- Determinar materias disponibles
- Calcular niveles académicos mínimos

# 2. Justificación de la Estructura de Datos

La estructura de datos seleccionada para el proyecto es un Grafo Dirigido Acíclico (DAG), ya que permite representar correctamente las dependencias existentes entre materias universitarias.

Cada nodo del grafo representa una materia y cada arista dirigida representa una relación de prerrequisito entre asignaturas.

La estructura es dirigida porque las dependencias tienen una dirección específica. Por ejemplo:

```text
Programación 1 → Estructura de Datos
```

Esto significa que Programación 1 debe aprobarse antes de cursar Estructura de Datos.

Además, el grafo debe ser acíclico, ya que una dependencia circular haría imposible completar correctamente la malla curricular.

---

## 2.1 ¿Por qué no usar otras estructuras?

### Árboles

Los árboles no son adecuados porque una materia puede tener múltiples prerrequisitos. Esto rompe la estructura jerárquica simple de un árbol tradicional.

### Listas

Las listas lineales no permiten representar relaciones complejas de dependencia entre materias.

### DAG

El DAG es la estructura más adecuada porque:

- Permite múltiples dependencias
- Mantiene relaciones dirigidas
- Soporta ordenamiento topológico
- Facilita detección de ciclos
- Representa correctamente prerrequisitos académicos

# 3. Análisis de Complejidad

## 3.1 Ordenamiento Topológico (Kahn)

El algoritmo de Kahn recorre cada nodo y cada arista del grafo una sola vez.

Complejidad temporal:

```text
O(V + E)
```

Donde:

- V representa el número de vértices (materias)
- E representa el número de aristas (prerrequisitos)

La complejidad es eficiente para mallas curriculares medianas y grandes.

---

## 3.2 Detección de ciclos (DFS)

La detección de ciclos usando DFS y coloreo de nodos también recorre cada nodo y arista una sola vez.

Complejidad temporal:

```text
O(V + E)
```

La utilización de colores (blanco, gris y negro) permite detectar ciclos de forma eficiente durante el recorrido profundo del grafo.

---

## 3.3 Materias disponibles

La búsqueda de materias disponibles requiere recorrer las materias y verificar sus prerrequisitos.

Complejidad temporal aproximada:

```text
O(V + E)
```

Esto permite validar rápidamente qué materias pueden cursarse dependiendo de las asignaturas aprobadas.

---

## 3.4 Cálculo de niveles

El cálculo de niveles académicos utiliza BFS sobre el DAG.

Complejidad temporal:

```text
O(V + E)
```

Cada materia y cada dependencia son procesadas una sola vez durante el recorrido.

---

## 3.5 Agregar materias y aristas

### Agregar nodo

```text
O(1)
```

La inserción de una materia en los diccionarios es inmediata.

### Agregar arista

```text
O(1)
```

La conexión entre materias y la actualización del in-degree se realiza en tiempo constante.


# 4. Requisitos Funcionales

## RF-01
Visualizar la malla curricular mediante un grafo dirigido.

## RF-02
Agregar materias y relaciones de prerrequisito.

## RF-03
Calcular un orden topológico válido para cursar materias.

## RF-04
Detectar ciclos o dependencias circulares dentro del grafo.

## RF-05
Mostrar las materias disponibles según las asignaturas aprobadas.

## RF-06
Calcular el semestre mínimo posible para cada materia.

---

# 5. Requisitos No Funcionales

## RNF-01
El sistema debe detectar ciclos de manera eficiente.

## RNF-02
El proyecto debe soportar mallas curriculares medianas y grandes.

## RNF-03
La lógica del DAG debe estar separada de la presentación.

## RNF-04
El código debe mantenerse modular, legible y comentado.

## RNF-05
La aplicación debe generar resultados comprensibles para el usuario.

# 6. Reflexión Técnica

Durante el desarrollo del proyecto fue posible comprender cómo los Grafos Dirigidos Acíclicos (DAG) pueden utilizarse para modelar problemas reales relacionados con dependencias y planificación académica.

Inicialmente, uno de los principales retos fue comprender correctamente la dirección de las aristas dentro del grafo, ya que una conexión invertida altera completamente el significado de los prerrequisitos y el funcionamiento del ordenamiento topológico.

La implementación permitió aplicar conceptos fundamentales de estructuras de datos como:

- Lista de adyacencia
- BFS (Breadth First Search)
- DFS (Depth First Search)
- Recursividad
- Ordenamiento topológico
- Detección de ciclos

Además, se comprendió la importancia del in-degree en el algoritmo de Kahn y cómo los recorridos BFS y DFS permiten resolver problemas reales de dependencias.

Otro aspecto importante fue la validación mediante casos de prueba, especialmente en escenarios con ciclos y múltiples prerrequisitos, lo cual permitió verificar el correcto comportamiento de la aplicación.

El proyecto también permitió identificar cómo los grafos son utilizados en sistemas reales como:

- Mallas curriculares universitarias
- Planificación de tareas
- Gestión de dependencias de software
- Sistemas de compilación
- Redes y rutas

---

# 7. Conclusiones

- Los DAG son estructuras altamente eficientes para representar dependencias académicas.
- El algoritmo de Kahn permite calcular órdenes válidos de cursado de materias.
- DFS con coloreo de nodos permite detectar ciclos de manera eficiente.
- BFS facilita el cálculo de niveles académicos mínimos.
- La combinación de estructuras de datos y algoritmos permite resolver problemas reales de planificación.

Además, el proyecto fortaleció conocimientos prácticos sobre grafos, complejidad algorítmica y organización modular de aplicaciones en Python.