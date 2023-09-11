# Week 2, September 2023

## Challenge 2 - Shortest Path in a Weighted Graph

Write a Python function `shortest_path(graph, start, end)` that takes a weighted directed graph, a starting node `start`, and an ending node `end` as input. The function should return the shortest path from the starting node to the ending node as a list of nodes. If there are multiple shortest paths, return any one of them.

*Instructions:*

1. Implement the shortest_path function to find the shortest path from the start node to the end node in the given weighted directed graph.
2. The graph is represented as an adjacency list where each node is a key, and its value is a list of tuples representing edges and their weights to other nodes.
3. You can assume that there is at least one path from the start to the end node.

*Example:*

```python
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': [],
}

result = shortest_path(graph, 'A', 'D')
# Should return ['A', 'B', 'D'] (shortest path from 'A' to 'D')

```
