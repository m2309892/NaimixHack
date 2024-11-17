from pyvis.network import Network
from sup_func.weights_normalization import *
from sup_func.team_percentage import team_percentage
import app.analitics.graph_with_thresholds as g_t


def graph_color_1(G):
    net = Network(notebook=True, cdn_resources='remote')  # notebook=True для Jupyter Notebook
    for node in G.nodes(data=True):
        net.add_node(node[0], label=node[1]['name'])
    for u, v, data in G.edges(data=True):
            edge_weight = data['weight']
            # Определяем цвет в зависимости от веса
            color = f'rgba(1, {255 - (120 + (100 - edge_weight )*4.5)}, {255 - (120 + (100 - edge_weight)*4.5)}, 1)'
            net.add_edge(u, v, title=f'Вес: {edge_weight}', width = 5, color=color)
    net.show('graph_1.html')



def team_select(names, edges, threshold = 70):
    edges = weights_normal(edges)
    
    # main_percent = team_percentage(edges)
    
    G = g_t.graph_with_thresholds(names, edges, threshold)
    e = (list(G.edges(data = True)))
    subgraph_percent = sum(edge[2]['weight'] for edge in e)/len(e)
    graph_color_1(G)
    return subgraph_percent
