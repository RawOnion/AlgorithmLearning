'''
贪心算法
贪心总是寻找目前最优的局部解
贪心要求局部解最终能得到全局最优解同时后续状态不能影响到当前状态

选择最少的广播台把所有的州都覆盖掉
1. 选出的广播台覆盖最多未覆盖的州
2. 重复第一步，直到覆盖所有的州
'''

def greed(states_needed,stations):
    #最终选择的广播台
    final_stations=set()
    while states_needed:
        #选出覆盖最多未覆盖的州的广播电视台
        best_stations=None
        states_covered=set()
        for station,states_for_station in stations.items():
            #求两个集合的交集
            covered=states_needed&states_for_station
            if len(covered)>len(states_covered):
                best_stations=station
                states_covered=covered
        final_stations.add(best_stations)
        print(best_stations)
        del stations[best_stations]
        states_needed-=states_covered
    return final_stations


if __name__=="__main__":
    #需要的州
    states_needed=set(["mt","wa","or","id","nv","ut","ca","az"])
    #可供选择的广播台
    stations={}
    stations["kone"]=set(["id","nv","ut"])
    stations["ktwo"]=set(["wa","id","mt"])
    stations["kthree"]=set(["or","nv","ca"])
    stations["kfour"]=set(["nv","ut"])
    stations["kfive"]=set(["ca","az"])

    print(greed(states_needed,stations))
