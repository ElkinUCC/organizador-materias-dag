"""
Proyecto: Organizador de Materias Universitarias usando DAG

Autor:
Elkin Augusto Amador Padilla

Descripción:
Implementación de un Grafo Dirigido Acíclico (DAG)
para modelar prerrequisitos académicos.

Incluye:
- Ordenamiento topológico (Kahn)
- Detección de ciclos (DFS)
- Materias disponibles
- Cálculo de niveles académicos
"""

from collections import deque


class DAG:
    """
    Grafo Dirigido Acíclico (DAG)
    para representar materias y prerrequisitos.
    """

    # ==================================================
    # CONSTRUCTOR
    # ==================================================

    def __init__(self):
        """
        Inicializa la estructura principal del grafo.

        graph:
            Lista de adyacencia.
            Guarda las conexiones entre materias.

        in_degree:
            Guarda cuántos prerrequisitos
            tiene cada materia.
        """

        # Lista de adyacencia
        self.graph = {}

        # Grado de entrada de cada nodo
        self.in_degree = {}

    # ==================================================
    # AGREGAR NODO
    # ==================================================

    def add_node(self, subject):
        """
        Agrega una materia al grafo.

        Parámetro:
            subject -> nombre de la materia
        """

        # Verificar si la materia ya existe
        if subject not in self.graph:

            # Crear lista vacía de vecinos
            self.graph[subject] = []

            # Inicialmente no tiene prerrequisitos
            self.in_degree[subject] = 0

    # ==================================================
    # AGREGAR ARISTA
    # ==================================================

    def add_edge(self, prerequisite, subject):
        """
        Agrega una relación de prerrequisito.

        prerequisite -> subject

        Ejemplo:
            Programación 1 -> Estructura de Datos
        """

        # Crear nodos automáticamente
        # si aún no existen

        if prerequisite not in self.graph:
            self.add_node(prerequisite)

        if subject not in self.graph:
            self.add_node(subject)

        # Agregar conexión entre materias
        self.graph[prerequisite].append(subject)

        # Aumentar el in-degree
        # de la materia dependiente
        self.in_degree[subject] += 1

    # ==================================================
    # ELIMINAR NODO
    # ==================================================

    def delete_node(self, subject):
        """
        Elimina una materia del grafo.

        También elimina todas las conexiones
        relacionadas con la materia.
        """

        # Verificar si existe
        if subject not in self.graph:

            print(f"\nLa materia '{subject}' no existe.\n")
            return

        # ==============================================
        # ELIMINAR CONEXIONES ENTRANTES
        # ==============================================

        for node in self.graph:

            if subject in self.graph[node]:

                # Eliminar conexión
                self.graph[node].remove(subject)

                # Reducir in-degree
                self.in_degree[subject] -= 1

        # ==============================================
        # ELIMINAR CONEXIONES SALIENTES
        # ==============================================

        for neighbor in self.graph[subject]:

            self.in_degree[neighbor] -= 1

        # ==============================================
        # ELIMINAR NODO
        # ==============================================

        del self.graph[subject]
        del self.in_degree[subject]

        print(f"\nMateria '{subject}' eliminada correctamente.\n")

    # ==================================================
    # MOSTRAR GRAFO
    # ==================================================

    def print_graph(self):
        """
        Imprime la lista de adyacencia
        del grafo.
        """

        print("\nGRAFO DE MATERIAS:\n")

        for subject in self.graph:
            print(f"{subject} -> {self.graph[subject]}")

    # ==================================================
    # ORDENAMIENTO TOPOLOGICO
    # ==================================================

    def topological_sort(self):
        """
        Implementa el algoritmo de Kahn
        para obtener un orden topológico.

        Retorna:
            Lista con el orden válido
            para cursar materias.
        """

        # Copia temporal del in-degree
        # para no modificar el original
        in_degree_copy = self.in_degree.copy()

        # Cola BFS
        queue = deque()

        # Lista resultado
        topological_order = []

        # Buscar materias sin prerrequisitos
        for subject in in_degree_copy:

            if in_degree_copy[subject] == 0:
                queue.append(subject)

        # Procesar cola
        while queue:

            # Extraer primer elemento
            current = queue.popleft()

            # Agregar al resultado final
            topological_order.append(current)

            # Revisar materias dependientes
            for neighbor in self.graph[current]:

                # Reducir in-degree
                # porque ya se "cumplió"
                # un prerrequisito
                in_degree_copy[neighbor] -= 1

                # Si queda libre de dependencias
                # se agrega a la cola
                if in_degree_copy[neighbor] == 0:
                    queue.append(neighbor)

        # Verificar si existe ciclo
        if len(topological_order) != len(self.graph):

            print("\nERROR: El grafo tiene un ciclo.\n")
            return []

        return topological_order

    # ==================================================
    # DETECCION DE CICLOS
    # ==================================================

    def has_cycle(self):
        """
        Detecta ciclos usando DFS
        y coloreo de nodos.

        Colores:
            WHITE -> no visitado
            GRAY  -> visitándose
            BLACK -> terminado
        """

        WHITE = 0
        GRAY = 1
        BLACK = 2

        # Todos los nodos empiezan en blanco
        color = {}

        for node in self.graph:
            color[node] = WHITE

        # ==============================================
        # DFS AUXILIAR
        # ==============================================

        def dfs(node):

            # Nodo en proceso
            color[node] = GRAY

            # Revisar vecinos
            for neighbor in self.graph[node]:

                # Si encontramos un nodo GRAY
                # existe un ciclo
                if color[neighbor] == GRAY:
                    return True

                # Si no ha sido visitado
                # seguimos DFS
                if color[neighbor] == WHITE:

                    if dfs(neighbor):
                        return True

            # Nodo completamente procesado
            color[node] = BLACK

            return False

        # Ejecutar DFS en todo el grafo
        for node in self.graph:

            if color[node] == WHITE:

                if dfs(node):
                    return True

        return False

    # ==================================================
    # MATERIAS DISPONIBLES
    # ==================================================

    def available_subjects(self, approved_subjects):
        """
        Retorna las materias disponibles
        según las materias aprobadas.

        Parámetro:
            approved_subjects -> lista
            de materias aprobadas
        """

        # Lista resultado
        available = []

        # Revisar todas las materias
        for subject in self.graph:

            # Ignorar materias ya aprobadas
            if subject in approved_subjects:
                continue

            # Lista de prerrequisitos
            prerequisites = []

            # Buscar quién apunta hacia la materia
            for node in self.graph:

                if subject in self.graph[node]:
                    prerequisites.append(node)

            # Suponer inicialmente
            # que todos los prerrequisitos
            # están completos
            all_prerequisites_completed = True

            # Verificar prerrequisitos
            for prerequisite in prerequisites:

                if prerequisite not in approved_subjects:

                    all_prerequisites_completed = False
                    break

            # Si cumple todo
            # agregar a disponibles
            if all_prerequisites_completed:
                available.append(subject)

        return available

    # ==================================================
    # CALCULAR NIVELES
    # ==================================================

    def calculate_levels(self):
        """
        Calcula el semestre mínimo
        para cada materia usando BFS.

        Retorna:
            Diccionario con niveles.
        """

        # Copia temporal del in-degree
        in_degree_copy = self.in_degree.copy()

        # Cola BFS
        queue = deque()

        # Diccionario de niveles
        levels = {}

        # Buscar materias iniciales
        for subject in self.graph:

            if in_degree_copy[subject] == 0:

                queue.append(subject)

                # Nivel inicial = 1
                levels[subject] = 1

        # BFS
        while queue:

            current = queue.popleft()

            # Revisar vecinos
            for neighbor in self.graph[current]:

                # Reducir in-degree
                in_degree_copy[neighbor] -= 1

                # El vecino queda
                # un nivel más abajo
                levels[neighbor] = levels[current] + 1

                # Si queda libre
                # entra a la cola
                if in_degree_copy[neighbor] == 0:
                    queue.append(neighbor)

        return levels

    # ==================================================
    # CAMINO CRITICO
    # ==================================================

    def critical_path(self):
        """
        Calcula el camino crítico del DAG.

        Retorna:
            Lista con la secuencia más larga
            de dependencias.
        """

        # Obtener orden topológico
        topological_order = self.topological_sort()

        # Si hay ciclo
        if not topological_order:
            return []

        # ==============================================
        # DISTANCIAS
        # ==============================================

        # Distancia máxima hasta cada nodo
        distance = {}

        # Nodo anterior
        previous = {}

        # Inicializar distancias
        for subject in self.graph:

            distance[subject] = 0
            previous[subject] = None

        # ==============================================
        # RECORRER EN ORDEN TOPOLOGICO
        # ==============================================

        for subject in topological_order:

            for neighbor in self.graph[subject]:

                # Si encontramos camino más largo
                if distance[subject] + 1 > distance[neighbor]:

                    # Actualizar distancia
                    distance[neighbor] = (
                        distance[subject] + 1
                    )

                    # Guardar nodo anterior
                    previous[neighbor] = subject

        # ==============================================
        # BUSCAR NODO FINAL
        # ==============================================

        end_node = max(
            distance,
            key=distance.get
        )

        # ==============================================
        # RECONSTRUIR CAMINO
        # ==============================================

        critical_path = []

        current = end_node

        while current is not None:

            critical_path.append(current)

            current = previous[current]

        # Invertir camino
        critical_path.reverse()

        return critical_path