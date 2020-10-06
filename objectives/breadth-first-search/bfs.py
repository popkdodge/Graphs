from queue import Queue
class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("nonexistent vert")
    
    def get_neighbors(self, vertex_id):
        
    
    def bft(self, starting_v_id):
        #empty queue
       
        # while the queue isn't empty
g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)
g.add_vertex(6)
g.add_vertex(7)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)
g.add_edge(4, 6)
g.add_edge(4, 7)
g.add_edge(5, 3)
g.add_edge(6, 3)
g.add_edge(7, 6)

#bft
g.bft(1)

