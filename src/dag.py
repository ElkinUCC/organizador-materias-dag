from collections import deque
class DAG:

    def __init__(self):
        """
        Constructor del grafo dirigido acíclico (DAG)
        """

        # Lista de adyacencia
        # Guarda qué materias dependen de otra
        self.graph = {}

        # Guarda el grado de entrada (in-degree)
        # de cada materia
        self.in_degree = {}

    def add_node(self, subject):
        """
        Agrega una materia al grafo
        """

        # Si la materia no existe
        if subject not in self.graph:

            # Crear lista vacía de conexiones
            self.graph[subject] = []

            # Inicialmente no tiene prerrequisitos
            self.in_degree[subject] = 0

    def add_edge(self, prerequisite, subject):
        """
        Agrega una relación de prerrequisito

        prerequisite -> subject
        """

        # Verificar que existan los nodos
        if prerequisite not in self.graph:
            self.add_node(prerequisite)

        if subject not in self.graph:
            self.add_node(subject)

        # Agregar conexión
        self.graph[prerequisite].append(subject)

        # Aumentar grado de entrada
        self.in_degree[subject] += 1

    def print_graph(self):
        """
        Imprime la lista de adyacencia
        """

        print("\nGRAFO DE MATERIAS:\n")

        for subject in self.graph:
            print(f"{subject} -> {self.graph[subject]}")
            
    def topological_sort(self):
        """
        Algoritmo de Kahn para orden topológico
        """

        # Copia del in-degree
        in_degree_copy = self.in_degree.copy()

        # Cola para nodos con in-degree 0
        queue = deque()

        # Agregar materias sin prerrequisitos
        for subject in in_degree_copy:
            if in_degree_copy[subject] == 0:
                queue.append(subject)

        # Lista del orden topológico
        topological_order = []

        # Procesar cola
        while queue:

            # Sacar materia actual
            current = queue.popleft()

            # Agregar al resultado
            topological_order.append(current)

            # Revisar vecinos
            for neighbor in self.graph[current]:

                # Reducir in-degree
                in_degree_copy[neighbor] -= 1

                # Si ya no tiene prerrequisitos
                if in_degree_copy[neighbor] == 0:
                    queue.append(neighbor)

        # Verificar si hubo ciclo
        if len(topological_order) != len(self.graph):
            print("\nERROR: El grafo tiene un ciclo.\n")
            return []

        return topological_order
    
    def has_cycle(self):
        """
        Detecta ciclos usando DFS y coloreo de nodos
        """

        # Estados de los nodos
        WHITE = 0
        GRAY = 1
        BLACK = 2

        # Todos empiezan no visitados
        color = {}

        for node in self.graph:
            color[node] = WHITE

        # DFS auxiliar
        def dfs(node):

            # Nodo en proceso
            color[node] = GRAY

            # Revisar vecinos
            for neighbor in self.graph[node]:

                # Si vecino está GRAY
                # encontramos un ciclo
                if color[neighbor] == GRAY:
                    return True

                # Si no ha sido visitado
                if color[neighbor] == WHITE:
                    if dfs(neighbor):
                        return True

            # Nodo terminado
            color[node] = BLACK

            return False

        # Ejecutar DFS en todos los nodos
        for node in self.graph:

            if color[node] == WHITE:

                if dfs(node):
                    return True

        return False
    
    def available_subjects(self, approved_subjects):
        """
        Retorna las materias disponibles
        según las materias aprobadas
        """

        available = []

        # Revisar todas las materias
        for subject in self.graph:

            # Ignorar materias ya aprobadas
            if subject in approved_subjects:
                continue

            # Buscar prerrequisitos
            prerequisites = []

            for node in self.graph:

                if subject in self.graph[node]:
                    prerequisites.append(node)

            # Verificar si todos los prerrequisitos
            # están aprobados
            valid = True

            for prerequisite in prerequisites:

                if prerequisite not in approved_subjects:
                    valid = False
                    break

            # Si cumple todo
            if valid:
                available.append(subject)

        return available
    
    def calculate_levels(self):
        """
        Calcula el nivel (semestre mínimo)
        de cada materia
        """

        # Copia del in-degree
        in_degree_copy = self.in_degree.copy()

        # Cola BFS
        queue = deque()

        # Diccionario de niveles
        levels = {}

        # Inicializar nodos fuente
        for subject in self.graph:

            if in_degree_copy[subject] == 0:

                queue.append(subject)

                # Materias iniciales = nivel 1
                levels[subject] = 1

        # BFS
        while queue:

            current = queue.popleft()

            # Revisar vecinos
            for neighbor in self.graph[current]:

                # Reducir in-degree
                in_degree_copy[neighbor] -= 1

                # Actualizar nivel
                levels[neighbor] = levels[current] + 1

                # Si queda libre
                if in_degree_copy[neighbor] == 0:
                    queue.append(neighbor)

        return levels