class Vertex:

    def __init__(self, value):
        self.value = value
        self.neighbours = []

    def __repr__(self):
        return str(self.value)


class Graph:

    def __init__(self):
        self.vertices = []

    def find(self, value):
        for vertex in self.vertices:
            if vertex.value == value:
                return vertex
        return None

    def add_vertex(self, value):
        if not self.find(value):
            self.vertices.append(Vertex(value))
        else:
            print(value, "already exist")

    def add_edge(self, source, target):
        source_v = self.find(source)
        target_v = self.find(target)

        if source_v and target_v:
            source_v.neighbours.append(target_v)
            target_v.neighbours.append(source_v)
        else:
            print("Some of", source, target, "are missing")

    def display(self):
        for vertex in self.vertices:
            print(vertex, ":", vertex.neighbours)

    def connected_components(self, source=None):

        queue = list()
        visited = set()

        components = []

        for vertex in self.vertices:

            if vertex not in visited:

                component = set()
                queue.append(vertex)
                visited.add(vertex)

                while len(queue) > 0:
                    vertex = queue.pop(0)

                    component.add(vertex)

                    for neighbour in vertex.neighbours:
                        if neighbour not in visited:
                            visited.add(neighbour)
                            queue.append(neighbour)

                components.append(component)

        return components

    def is_bipartite(self, source=None):

        queue = list()
        visited = set()

        red = set()
        green = set()

        for vertex in self.vertices:

            if vertex not in visited:

                queue.append(vertex)
                visited.add(vertex)

                # special focus here. We added first item as red
                red.add(vertex)

                while len(queue) > 0:
                    vertex = queue.pop(0)

                    for neighbour in vertex.neighbours:

                        # not visited items are to be divided
                        if neighbour not in visited:
                            if vertex in red:
                                green.add(neighbour)
                            if vertex in green:
                                red.add(neighbour)

                            visited.add(neighbour)
                            queue.append(neighbour)
                        # visited items are to be verified
                        else:
                            if vertex in red and neighbour in red:
                                return False
                            if vertex in green and neighbour in green:
                                return False

        return True


if __name__ == "__main__":

    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)

    graph.add_edge(1, 2)
    graph.add_edge(4, 3)

    print(graph.is_bipartite())

    graph.add_edge(1, 5)
    graph.add_edge(2, 5)

    print(graph.is_bipartite())
