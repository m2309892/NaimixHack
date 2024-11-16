def team_percentage(edges):
    av = 0
    k = 0
    for edge in edges:
        av += edge[2]
        k += 1
    return round(av/len(edges) , 2)

    
# сравнение процента команды до и после добавления нового человека
#изначальный общий процент команды влияет
#плюс метода : можно добавить бонус за хорошие отношения с букой!
#возвращает процент команды после добавления кандидата и то на сколько поднялся(полож значение)/упал процент(отриц значение)
def per_comparison(team_edges, cand_edges):
    poten_team_edges = team_edges + cand_edges
    difference = round(team_percentage(poten_team_edges)-team_percentage(team_edges),2)
    return team_percentage(poten_team_edges), difference
    #описание шкалы значений
    #print("difference < 0: the candidate is not suitable for the team\n 0 < difference < 5 :most likely there will be no conflicts\n 5 < difference < 11 : the candidate will suit the team\n 10 < difference: please, save your team, give the candidate job")



#среднее значение совместимости нового человека с каждым отдельно
#изначальный общий процент команды не влияет
def one_comparison(cand_edges):
    percent = team_percentage(cand_edges)
    return percent