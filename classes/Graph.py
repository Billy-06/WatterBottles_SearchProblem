import pydot

# Graph class
class Graph:
    def __init__(self, title, engine="dot"):
        self.title = title
        self.engine = engine
        self.graph = pydot.Dot(graph_type="digraph", label=title,
                               labelloc="t", fontsize="20", fontcolor="blue")

    def attr(self, name, value, shape=None):
        self.graph.set(name, value)
        if shape is not None:
            for node in self.graph.get_node_list():
                node.set("shape", shape)
        self.graph.get_node(name)[0].set("shape", shape)


    def node(self, name):
        self.graph.add_node(pydot.Node(name))

    def edge(self, source, target, label=None):
        self.graph.add_edge(pydot.Edge(source, target, label=label))

    def render(self, filename, view=False):
        self.graph.write(filename, format="png")
        if view:
            self.graph.write_png(filename)

