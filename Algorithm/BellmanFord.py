'''
Bellman-Ford
贝尔曼富德算法是为了解决在加权有向图中存在负权值的情况
其时间复杂度为O(V*E)比Dij的复杂度要高，但是可以发现负环

应用场景：单源最短路径

最短路径肯定是一个简单路径，不包含回路（正权值回路和负权值回路）
若图中存在未确认的顶点，则对边集合的一次迭代松弛后，会增加至少一个已确认的顶点，即图中某条最短路径长度会至少加一。
因此只需要执行的迭代次数最多为V-1次，如果有向图中存在负环则在第V循环后，存放最短路径的列表发生改变则一定存在负环。
'''

class BellmanFord(object):
    def __init__(self):
        #图结构
        self.G={}
        # 出度节点
        self.start_v = []
        # 入度节点
        self.end_v = []
        # 边集
        self.w = []
        #start节点到当前节点的距离
        self.dis={}
        #存储父节点
        self.parent={}
        self.inifity=float("inf")
    def init_graph(self,G,v0):
        for i in G.keys():
            self.parent[i]=None
            for k in G[i].keys():
                #存入start节点
                self.start_v.append(i)
                #存入end节点
                self.end_v.append(k)
                #存入start节点到end节点权值
                self.w.append(G[i][k])

        self.dis=dict((k,self.inifity) for k in G.keys())
        self.dis[v0]=0
        self.G=G

#核心代码部分
    def  bellmanFord(self):
        #执行V-1次迭代
        for i in range(len(self.G)-1):
            # 检测本轮松弛后dis是否发生变化
            check = 0
            for k in range(len(self.w)):
                if self.dis[self.start_v[k]]+self.w[k]<self.dis[self.end_v[k]]:
                    self.dis[self.end_v[k]]=self.dis[self.start_v[k]]+self.w[k]
                    self.parent[self.end_v[k]]=self.start_v[k]
                    check=1
            if check:
                break
        #检测是否含有负环
        flag=0
        for i in range(len(self.w)):
            if self.dis[self.start_v[i]]+self.w[i]<self.dis[self.end_v[i]]:
                flag=1
                break
        if flag:
            print("存在负环!")
            return None

    def get_route(self):
        print("最优路径为：")
        for i in self.parent.keys():
            #打印父节点
            if self.parent[i]:
                print(self.parent[i],end="--->")
        #打印最后一个节点
        print(list(self.parent.keys())[-1])

if __name__=="__main__":
    g=BellmanFord()
    G = {1:{2:-3, 5:5},
        2:{3:2},
        3:{4:3},
        4:{5:2},
        5:{}}
    g.init_graph(G,1)
    g.bellmanFord()
    print(g.dis)
    g.get_route()
