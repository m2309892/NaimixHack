from Graph import *
def temp_graph_to_html(G, cand_id, file_name):
    net = Network(notebook=True, cdn_resources='remote')  # notebook=True для Jupyter Notebook
    for node in G.nodes(data=True):
        net.add_node(node[0], label=node[1]['name'])

    # Добавляем ребра в Pyvis с учетом цветов
    for u, v, data in G.edges(data=True):
        edge_weight = data['weight']
        if u == cand_id or v == cand_id:
            # Определяем цвет в зависимости от веса
            color = f'rgba(1, {255 - (edge_weight * 2.5)}, {255 - (edge_weight * 2.5)}, 1)'
            net.add_edge(u, v, title=f'Вес: {edge_weight}', width = 5, color=color)
        else:
            net.add_edge(u, v, title=f'Вес: {edge_weight}', width = 5, color='black')
    net.show(file_name) 
#сначала создаем граф команды, убираем ребра с маленькими весами
team_graph = get_graph(names, edges)
set_threshold(team_graph, 70)

#добавляем узел кондидата
cand_id, cand_name = list(cand.items())[0]
team_graph.add_node(cand_id, name = cand_name)

#добавляем взвешенные ребр к каждому члену команды от кардидата
team_graph.add_weighted_edges_from(cand_edge)
#ребра от кандидата удалять не будем, цветом покажем разброс
temp_graph_to_html(team_graph, cand_id, 'graph.html')#cand_id чтобы понять какие ребра как окрашивать