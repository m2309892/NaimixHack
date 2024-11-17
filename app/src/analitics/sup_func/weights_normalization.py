#Results: 
# - From 0 to 5 = Null relationship 
# - From 5 a 10 = Mediocre relationship 
# - From 10 to 15 = Important relationship 
# - From 15 to 20 = Very important relationship 
# - From 20 to su = Exceptional relationshi
def weights_normal(edges: tuple):
    new_edges = []
    #print('normalized')
    for edge in edges:
        if edge[2] <= 20:
            new_edge = (edge[0], edge[1], int((edge[2] *100) / 20))
        else:
            new_edge = (edge[0], edge[1], 100)
        new_edges.append(new_edge)
    return new_edges