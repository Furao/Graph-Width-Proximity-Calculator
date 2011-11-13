
class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.points = {}
        self.eccentricities = {}

        self.width = 0
        self.proximity = 0
        self.key_vertex = '0'
        
    def main(self):
        """Walk the matrix."""
        for i, row in enumerate(self.graph):
            self.curr_point = {}
            for j, column in enumerate(row):
                if column == 1 and j != i:
                    self.curr_point[str(j)] = 1
                    self.walk(j, [i], 2)
            del self.curr_point[str(i)]
            self.points[str(i)] = self.curr_point
        
        self.get_eccentricities()
        self.get_width()
        self.get_proximity()

    def walk(self, row_num, visited_rows, edges):
        for j, column in enumerate(self.graph[row_num]):
            if column == 1 and j != row_num:
                if str(j) in self.curr_point:
                    if self.curr_point[str(j)] > edges:
                        self.curr_point[str(j)] = edges        
                else:
                    self.curr_point[str(j)] = edges
                if j not in visited_rows:
                    self.walk(j, visited_rows+[row_num], edges+1)

    def get_width(self):
        for k, v in self.eccentricities.iteritems():
            if v > self.width:
                self.width = v

    def get_proximity(self):
        self.proximity = self.eccentricities['0']
        for k, v in self.eccentricities.iteritems():
            if v < self.proximity:
                self.proximity = v
                self.key_vertex = k
        
    def get_eccentricities(self):
        for k, v in self.points.iteritems():
            maximum = 0
            for vertex, edges in v.iteritems():
                if int(edges) > maximum:
                    maximum = int(edges)
            self.eccentricities[k] = maximum
            # for x in i:
            #     print x

if __name__ == '__main__':
    
    g = [ \
        [0, 1, 0, 1], \
        [1, 0, 1, 1], \
        [0, 1, 0, 0], \
        [1, 1, 0, 0]  \
        ]

    # for row in g:
    #     print row

    expected_width = 2
    expected_prox = 1

    curr_graph = Graph(g)

    curr_graph.main()

    print "Width: %i" % curr_graph.width
    print "Proximity: %i" % curr_graph.proximity
    print "Key Vertex: V%i" % (int(curr_graph.key_vertex) + 1)

    #print curr_graph.eccentricities