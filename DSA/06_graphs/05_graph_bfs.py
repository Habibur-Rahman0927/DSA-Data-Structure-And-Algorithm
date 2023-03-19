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

    def BSF(self, source):
        visited = set()
        queue = deque([source])
        visited.add(source)

        while queue:
            vertex = queue.popleft()
            print(vertex, end="")

            for neighbour in self.adj_list[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

    # def BFS(self, source):
    #     visited = set()
    #     queue = deque([source])
    #     visited.add(source)
    #     self.bfs_helper(queue, visited)
        # while queue:
        #     vertex = queue.popleft()
        #     print(vertex, end="")

        #     for neighbour in self.adj_list[vertex]:
        #         if neighbour not in visited:
        #             visited.add(neighbour)
        #             queue.append(neighbour)

    # def bfs_helper(self, queue, visited):
    #     while queue:
    #         vertex = queue.popleft()
    #         print(vertex, end="")

    #         for neighbour in self.adj_list[vertex]:
    #             if neighbour not in visited:
    #                 visited.add(neighbour)
    #                 queue.append(neighbour)


# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }



my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A','B')
my_graph.add_edge('A','C')
my_graph.add_edge('A','D')
my_graph.add_edge('B','D')
my_graph.add_edge('C','D')

my_graph.BSF('A')
print("\n")
my_graph.print_graph()

