import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        """Initialize a tree node.

        :param key: The value of the node.
        :param color: The color of the node.
        """

        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """Recursively add nodes and edges from the binary tree to the graph.

    :param graph: NetworkX directed graph.
    :param node: Current tree node.
    :param pos: Dictionary to store node positions.
    :param x: x-coordinate of the current node.
    :param y: y-coordinate of the current node.
    :param layer: current depth level in the tree.
    :return: updated graph.
    """

    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    """Draw the binary tree using NetworkX and matplotlib.

    :param tree_root: The root node of the tree.
    """
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def list_to_heap_tree(arr: list[int], element_index=0):
    """Convert a list representation of a binary heap to a tree.

    :param arr: List of integers representing the binary heap.
    :param element_index: Index of the current element in the list.
    :return: The root node of the binary heap tree.
    """
    if element_index >= len(arr):
        return None
    # Create a new node for the current element.
    node = Node(arr[element_index])

    # Recursively build the left and right subtrees.
    node.left = list_to_heap_tree(arr, 2 * element_index + 1)
    node.right = list_to_heap_tree(arr, 2 * element_index + 2)
    return node
