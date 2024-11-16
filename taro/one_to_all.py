from pyvis.network import Network
from sup_func.weights_normalization import *
from sup_func.team_percentage import team_percentage
import graph_with_thresholds as g_t

def all_percentage(team_edges, cand_edges):
    team_edges = weights_normal(team_edges)
    cand_edges = weights_normal(cand_edges)
    team_percent = team_percentage(team_edges)
    full_percent = team_percentage(team_edges + cand_edges)
    cand_percent = team_percentage(cand_edges)
    return round(full_percent-team_percent,2), full_percent, cand_percent


def graph_color_2(G, cand_id):
    net = Network(notebook=True, cdn_resources='remote')  # notebook=True для Jupyter Notebook
    for node in G.nodes(data=True):
        if node[0] == cand_id:
            net.add_node(node[0], label=node[1]['name'], color = 'red')
        else:
            net.add_node(node[0], label=node[1]['name'])
    for u, v, data in G.edges(data=True):
        edge_weight = data['weight']
        if u == cand_id or v == cand_id:
            # Определяем цвет в зависимости от веса
            color = f'rgba(1, {255 - (edge_weight * 2.5)}, {255 - (edge_weight * 2.5)}, 1)'
            net.add_edge(u, v, title=f'Вес: {edge_weight}', width = 5, color=color)
        else:
            net.add_edge(u, v, title=f'Вес: {edge_weight}', width = 5, color='black')
    net.show('graph_1.html')

def team_select(team_names, team_edges, cand, cand_edges, threshold = 60):
    team_edges = weights_normal(team_edges)
    #создаем граф команды
    G = g_t.graph_with_thresholds(team_names, team_edges, threshold)

    #добавляем узел кандидата 
    cand_id, cand_name = list(cand.items())[0]
    G.add_node(cand_id, name = cand_name)

    cand_edges = weights_normal(cand_edges)
    #добавляем взвешенные ребр к каждому члену команды от кардидата
    G.add_weighted_edges_from(cand_edges)

    graph_color_2(G, cand_id)

