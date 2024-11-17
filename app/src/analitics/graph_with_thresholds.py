import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
def graph_with_thresholds(names, edges, threshold):
    G = get_graph(names, edges)
    set_threshold(G, threshold=threshold)
    return G
def get_graph(names: dict, edges):
    G = nx.Graph()
    #вершины
    for name_id, name in names.items():
        G.add_node(name_id, name=name)
    #взвешенные ребра 
    G.add_weighted_edges_from(edges)
    return G
def set_threshold(G, threshold):#remove all edges of the graph with a weight below the threshold
    edges_to_remove = [(u, v) for u, v, data in G.edges(data=True) if data['weight'] < threshold]
    G.remove_edges_from(edges_to_remove)