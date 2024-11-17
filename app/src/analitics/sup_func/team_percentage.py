def team_percentage(edges):
    av = 0
    k = 0
    for edge in edges:
        av += edge[2]
        k += 1
    return round(av/len(edges) , 2)