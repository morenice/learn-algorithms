# -*- encoding: utf-8 -*-
import copy


class Graph:
    def __init__(self):
        self.vertex_map = dict()

    def add(self, name, vertex):
        self.vertex_map[name] = vertex

    def find(self, name):
        return self.vertex_map[name]


class Vertex:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.distance = -1  # -1 is INFINITE
        self.visit = False


class VertexEdgeMap:
    def __init__(self):
        self.edge_map = dict()

    def _get_edge_list(self, source_vertex_name):
        try:
            edge_list = self.edge_map[source_vertex_name]
        except KeyError:
            self.edge_map[source_vertex_name] = list()
            edge_list = self.edge_map[source_vertex_name]

        return edge_list

    def add(self, source_vertex_name, dest_vertex_name):
        edge_list = self._get_edge_list(source_vertex_name)
        if dest_vertex_name not in edge_list:
            edge_list.append(dest_vertex_name)

        edge_list = self._get_edge_list(dest_vertex_name)
        if source_vertex_name not in edge_list:
            edge_list.append(source_vertex_name)

    def get_vertexs(self, source_vertex_name):
        return self.edge_map[source_vertex_name]


def BFS(graph, vertex_edge, start_v_name):
    """Breadth First Search"""
    for i, vertex in graph.vertex_map.items():
        vertex.parent = None
        vertex.distance = -1
        vertex.visit = False

    queue = list()
    start_vertex = graph.find(start_v_name)
    start_vertex.distance = 0
    queue.append(start_vertex)

    visit_vertex_list = list()
    visit_vertex_list.append(start_vertex.name)

    while len(queue) > 0:
        current = queue[0]
        del(queue[0])

        for vertex_name in vertex_edge.get_vertexs(current.name):
            vertex = graph.find(vertex_name)
            if vertex.distance == -1:
                vertex.distance = current.distance+1
                vertex.visit = True
                vertex.parent = current
                queue.append(vertex)

                visit_vertex_list.append(vertex.name)

    return visit_vertex_list


def DFS(graph, vertex_edge, start_v_name):
    """Depth First Search"""
    for i, vertex in graph.vertex_map.items():
        vertex.parent = None
        vertex.distance = -1
        vertex.visit = False

    stack = list()
    start_vertex = graph.find(start_v_name)
    stack.append(start_vertex)

    visit_vertex_list = list()

    while len(stack) > 0:
        current = stack.pop()

        if current.visit is not True:
            current.visit = True
            visit_vertex_list.append(current.name)

            for vertex_name in vertex_edge.get_vertexs(current.name):
                vertex = graph.find(vertex_name)
                stack.append(vertex)

    return visit_vertex_list


if __name__ == '__main__':
    # first line
    input_line = input().split(' ')
    vertex_count = int(input_line[0])
    trunk_count = int(input_line[1])
    start_vertex_name = int(input_line[2])

    # init graph
    graph = Graph()
    for i in range(1, vertex_count+1):
        vertex = Vertex(i)
        graph.add(i, vertex)

    # init vertex-edge
    vertex_edge = VertexEdgeMap()
    for i in range(1, trunk_count+1):
        input_trunk_line = input().split(' ')
        source_vertex = int(input_trunk_line[0])
        dest_vertex = int(input_trunk_line[1])
        vertex_edge.add(source_vertex, dest_vertex)

    l = DFS(graph, vertex_edge, start_vertex_name)
    print(" ".join('%d' % x for x in l))

    l = BFS(graph, vertex_edge, start_vertex_name)
    print(" ".join('%d' % x for x in l))
