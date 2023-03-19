from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def bfs_disconnected(self, graph):
        visited = set()
        for vertex in graph:
            if vertex not in visited:
                queue = deque([vertex])
                visited.add(vertex)
                while queue:
                    vertex = queue.popleft()
                    print(vertex, end="")

                    for neighbour in graph[vertex]:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            queue.append(neighbour)


my_graph = Graph()
# my_graph.add_vertex('A')
# my_graph.add_vertex('B')
# my_graph.add_vertex('C')
# my_graph.add_vertex('D')
# my_graph.add_vertex('E')
# my_graph.add_vertex('F')
# my_graph.add_vertex('G')
# my_graph.add_vertex('H')
# my_graph.add_vertex('I')
# my_graph.add_vertex('J')

# my_graph.add_edge('A','B')
# my_graph.add_edge('A','C')
# my_graph.add_edge('B','D')
# my_graph.add_edge('B','E')
# my_graph.add_edge('C','F')
# my_graph.add_edge('E','F')
# my_graph.add_edge('G','H')
# my_graph.add_edge('H','I')
# my_graph.add_edge('H','J')
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': [],
    'G': ['H'],
    'H': ['I', 'J'],
    'I': [],
    'J': []
}

# my_graph.BFS('A')
# print("\n")
my_graph.bfs_disconnected(graph)
print("\n")
my_graph.print_graph()

