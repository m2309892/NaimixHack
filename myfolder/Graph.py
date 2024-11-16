import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from pyvis.network import Network
#names = {id:name_of_client}
def get_graph(names: dict, edges):#добав переменные исп в поиске процентов
    G = nx.Graph()
    #вершины
    for name_id, name in names.items():
        G.add_node(name_id, name=name)
    
    #взвешенные ребра 
    G.add_weighted_edges_from(edges)
    #G.add_weighted_edges_from([(i, j, get_edge_weight(i,j)) for i in G.nodes() for j in G.nodes() if i < j])
    return G
def set_threshold(G, threshold):#remove all edges of the graph with a weight below the threshold
    edges_to_remove = [(u, v) for u, v, data in G.edges(data=True) if data['weight'] < threshold]
    G.remove_edges_from(edges_to_remove)
def graph_to_html(G, file_name):
    net = Network(notebook=True, cdn_resources='remote')  # notebook=True для Jupyter Notebook
    for node in G.nodes(data=True):
        net.add_node(node[0], label=node[1]['name'])

    # Добавляем ребра в Pyvis с учетом цветов
    for u, v, data in G.edges(data=True):
        edge_weight = data['weight']
        # Определяем цвет в зависимости от веса
        color = f'rgba(1, {255 - (edge_weight * 2.5)}, {255 - (edge_weight * 2.5)}, 1)'
        net.add_edge(u, v, title=f'Вес: {edge_weight}', width = 5, color=color)
    net.show(file_name) 
def create_Graph_with_threshold(names, edges, threshold, file_name = 'graph.html'):
    Graph = get_graph(names,edges)
    set_threshold(Graph, threshold)
    graph_to_html(Graph, file_name)
