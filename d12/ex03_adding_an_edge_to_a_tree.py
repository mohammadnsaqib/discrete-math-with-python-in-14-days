"""What one more edge does to a tree, and what one fewer does."""
import networkx as nx

from dmkit.graph import Graph, components, path_graph
from dmkit.tree import has_cycle, is_tree

tree = path_graph(5)
print(f"a line of 5: {tree.edges()}, a tree: {is_tree(tree)}")
print()
print(f"{'edge added':>14} {'edges':>7} {'a cycle now':>13} {'still a tree':>14} "
      f"{'cycles':>8}")
for a, b in [(0, 2), (0, 4), (1, 3), (2, 4)]:
    bigger = Graph(tree.vertices(), tree.edges() + [(a, b)])
    other = nx.Graph()
    other.add_nodes_from(bigger.vertices())
    other.add_edges_from(bigger.edges())
    print(f"{str((a, b)):>14} {len(bigger.edges()):>7} {str(has_cycle(bigger)):>13} "
          f"{str(is_tree(bigger)):>14} {len(list(nx.simple_cycles(other))):>8}")
print()
print(f"{'edge removed':>14} {'edges':>7} {'pieces':>8} {'still a tree':>14}")
for edge in tree.edges():
    smaller = Graph(tree.vertices(), [e for e in tree.edges() if e != edge])
    print(f"{str(edge):>14} {len(smaller.edges()):>7} {len(components(smaller)):>8} "
          f"{str(is_tree(smaller)):>14}")
