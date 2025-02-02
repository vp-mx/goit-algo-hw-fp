import uuid
import networkx as nx
import matplotlib.pyplot as plt

from shared_funcs import list_to_heap_tree, draw_tree


def visualize_heap(heap_list: list[int]) -> None:
    """
    Visualize a binary heap by building its tree and drawing it.

    :param heap_list: List of integers representing the binary heap.
    """
    # Build the binary heap tree from the list.
    heap_tree = list_to_heap_tree(heap_list)
    if heap_tree is not None:
        draw_tree(heap_tree)
    else:
        print("Heap is empty.")


# Example usage:
if __name__ == "__main__":
    # Example binary heap represented as a list.
    heap_list = [10, 12, 15, 20, 17, 25, 30]
    visualize_heap(heap_list)
