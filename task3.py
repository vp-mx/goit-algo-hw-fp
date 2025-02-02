import heapq
from typing import Dict, List, Tuple, Optional


class Graph:
    def __init__(self) -> None:
        """Initialize an empty graph.
        The graph is represented as a dictionary where keys are vertices and values
        are lists of tuples representing edges in the form (neighbor, weight).
        """
        self.edges: Dict[str, List[Tuple[str, int]]] = {}

    def add_edge(self, from_vertex: str, to_vertex: str, weight: int) -> None:
        """Add edge to the graph.

        Since the graph is undirected, the edge is added in both directions.

        :param from_vertex: The starting vertex.
        :param to_vertex: The ending vertex.
        :param weight: The weight of the edge.
        """
        # If the vertex is not in the graph, add it with an empty list.
        if from_vertex not in self.edges:
            self.edges[from_vertex] = []
        if to_vertex not in self.edges:
            self.edges[to_vertex] = []
        # Add the edge in both directions.
        self.edges[from_vertex].append((to_vertex, weight))
        self.edges[to_vertex].append((from_vertex, weight))

    def dijkstra(self, start: str) -> Tuple[Dict[str, float], Dict[str, Optional[str]]]:
        """Compute the shortest distances from the start node to every other node
        using Dijkstra's algorithm.

        :param start: The starting vertex.
        :return: A tuple of two dictionaries:
                 - distances: shortest distance from start to each vertex.
                 - previous: the previous vertex in the shortest path.
        """
        # Initialize distances: set all to infinity except the start vertex.
        distances = {vertex: float("infinity") for vertex in self.edges}
        previous = {vertex: None for vertex in self.edges}
        distances[start] = 0

        # Priority queue to hold vertices to explore.
        # Each element is a tuple (distance from start, vertex)
        heap: List[Tuple[float, str]] = [(0, start)]

        while heap:
            # Get the vertex with the smallest distance
            current_distance, current_vertex = heapq.heappop(heap)

            # Skip if we already found a better path
            if current_distance > distances[current_vertex]:
                continue

            # Check all the neighbors of the current vertex.
            for neighbor, weight in self.edges[current_vertex]:
                distance = current_distance + weight

                # If a shorter path to neighbor is found, update its distance and previous vertex.
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_vertex
                    heapq.heappush(heap, (distance, neighbor))

        return distances, previous


if __name__ == "__main__":

    graph = Graph()
    graph.add_edge("A", "B", 1)
    graph.add_edge("A", "C", 4)
    graph.add_edge("B", "C", 2)
    graph.add_edge("B", "D", 5)
    graph.add_edge("C", "D", 1)
    graph.add_edge("D", "E", 3)

    start_vertex = "A"
    distances, previous = graph.dijkstra(start_vertex)

    print(f"Distances from vertex {start_vertex} to all other vertices:")
    for vertex, distance in distances.items():
        print(f"Distance to vertex {vertex}: {distance}")
