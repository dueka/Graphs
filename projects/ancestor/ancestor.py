class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop()
        else:
            return None

    def size(self):
        return len(self.queue)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, ancestor_id):
        if ancestor_id not in self.vertices:
            return
        self.vertices[ancestor_id] = set()

    def add_edge(self, children, parents):
        if parents not in self.vertices[children] and parents in self.vertices and children in self.vertices:
            self.vertices[children].add(parents)
        else:
            raise IndexError("Vertex does not exist!")

    def get_ancestors(self, ancestor_id):
        return self.vertices[ancestor_id]


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    # instantiate a BFT
    q = Queue()
    q.enqueue([starting_node])
    max_length = 1
    earliest_ancestor = -1
    while q.size() > 0:
        path = q.dequeue()
        last_vertex = path[-1]
        if (len(path)) > max_length and last_vertex < earliest_ancestor:
            earliest_ancestor = last_vertex
