'''
求加权图中总权重最小的路径问题：狄克斯特拉算法(Dijkstra)。
该算法只适合没有负权重的有向图

狄克斯特拉算法核心假设是：对于处理过的节点，没有前往该节点更短的路径。
算法步骤：
1. 可在最短时间内前往的节点。
2. 对于该节点的邻居,检查是否有前往它们的更短路径,如果有，就更新其开销。
3. 重复这个过程直到对图中每个节点都执行一次。
4. 计算最终路径。

应用场景：
单源最短路径

G(V,E)   V为顶点数量,E为边的数量
该实现Dij算法的时间复杂度O(V^2)
Dij的斐波那契堆的时间复杂度为O(E+VlogV)
'''

class Dijkstra(object):
    def __init__(self):
        self.graph={}#存放加权有向图关系
        self.costs={}#存放节点开销
        self.parent={}#存放当前节点的父节点，用于得到最终路径
        #存放已经访问过的节点
        self.processed=[]
        self.infinity=float("inf")
    #初始化整个加权有向图
    def init_graph(self,graph_arr):
        for i in graph_arr:
            self.graph[i]={}

    #初始化有向图的关系
    def init_graph_relation(self,key,graph_dic):
        self.graph[key]=graph_dic

    def init_costs(self,graph_costs):
        self.costs=graph_costs

    def init_parent(self,graph_parent):
        self.parent=graph_parent

    #狄克斯特拉算法主体部分
    def dijkstra(self):
        node=self.find_lowest_cost_node(self.costs)
        #该循环的执行次数为self.costs{}字典中元素的个数，就是图中节点个数
        while node is not None:
            #得到该节点的花费
            cost=self.costs[node]
            #依次获取该节点的出度边
            for i in self.graph[node].keys():
                new_cost=cost+self.graph[node][i]
                #如果经过该节点得到的花费大于新花费，则更新花费字典
                if self.costs[i]>new_cost:
                    self.costs[i]=new_cost
                    self.parent[i]=node
            self.processed.append(node)
            node=self.find_lowest_cost_node(self.costs)

    #找到花费最小的节点
    def find_lowest_cost_node(self,costs):
        lowest_cost=self.infinity
        lowest_cost_node=None
        #从字典中找到最小值
        for i in self.costs.keys():
            if i not in self.processed and costs[i]<lowest_cost:
                lowest_cost_node=i
                lowest_cost=costs[i]

        return lowest_cost_node


    #获取路线
    def get_route(self):
        node="end"
        shortest_path=["end"]
        while self.parent[node]!="start":
            shortest_path.append(self.parent[node])
            node=self.parent[node]
        shortest_path.append("start")
        return list(reversed(shortest_path))

if __name__=="__main__":
    d=Dijkstra()
    #初始化加权有向图
    d.init_graph(["start","A","B","end"])
    d.init_graph_relation("start",{"A":6,"B":2})
    d.init_graph_relation("A", {"end": 1})
    d.init_graph_relation("B", {"A": 3, "end": 5})
    d.init_graph_relation("end",{}) #这里end节点没有邻节点不能用None来代替
    #初始化花费，开始节点到其它节点的开销
    d.init_costs({"start":0,"A":d.infinity,"B":d.infinity,"end":d.infinity})
    #初始化父子路径节点关系
    d.init_parent({"A":None,"B":None,"end":None})

    d.dijkstra()

    print(d.get_route())





