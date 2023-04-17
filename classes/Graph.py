"""

__init__(self, title, engine="dot"): The class constructor method that initializes a 
new instance of the graph. It takes two arguments: 
    > "title" (a string representing the title of the graph) and 
    > "engine" (a string representing the layout engine to use, with "dot" being the default). 
Inside the constructor, a new instance of the Pydot Dot class is created, with 
"digraph" as the graph type, and with the provided title, label location, font size, and font color.

attr(self, name, value, shape=None): A method to set a graph attribute (name and value) 
and optionally apply a shape attribute to all nodes. The method takes three arguments: 
    > "name" (a string representing the name of the attribute to set), 
    > "value" (the value of the attribute), and 
    > "shape" (an optional string representing the shape to apply to all nodes).

node(self, name): A method to add a new node to the graph. It takes one argument: 
    > "name" (a string representing the name of the node).

edge(self, source, target, label=None): A method to add a new edge to the graph, 
connecting two nodes. It takes two arguments: 
    > "source" (a string representing the name of the source node) and 
    > "target" (a string representing the name of the target node). 
It also has an optional "label" argument, representing the label to put on the edge.

render(self, filename, view=False): A method to render and save the graph to a file in 
PNG format. It takes two arguments: "filename" (a string representing the name of the 
output file) and "view" (an optional boolean representing whether to view the output 
file after saving it). The method writes the graph in PNG format and saves it with the 
provided filename. If "view" is True, it also opens the PNG file.

"""
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

