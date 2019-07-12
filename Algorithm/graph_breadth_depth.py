'''
图中的广度优先遍历与深度优先遍历
本实例代码为无向图
有向图与无向图最主要的区别在邻居节点字典中是不是互相包含
如果互相包含就是无向图
否则就是有向图

时间复杂度：
深度优先与广度优先时间复杂度都是O(顶点数+边数)
广度优先是先沿着边前行，同时每个节点都需要入队列，因此时间复杂度为O(顶点数+边数)
'''
from collections import deque
class Graph(object):
    def __init__(self):
        self.node_neighbors = {}

    def get_node_neighbors(self):
        return self.node_neighbors.keys()
    #创建邻居节点的key
    def add_nodes(self, nodelist):
        for node in nodelist:
            if not node in self.node_neighbors.keys():
                self.node_neighbors[node] = []

    # 为图中每一个节点添加邻居节点
    def add_edge(self, edge_node):
        u, v = edge_node
        #无向图中每一个节点添加邻居节点
        if (v not in self.node_neighbors[u]) and (u not in self.node_neighbors[v]):
            self.node_neighbors[u].append(v)

            if (u != v):
                self.node_neighbors[v].append(u)

    #深度优先搜索
    def depth_first_search(self, root=None):
        '''
        判断根节点的邻节点是否被访问过，没有则访问，并将该节点加入被访问列表中
        并访问该节点的邻节点
        '''
        #记载深度优先访问元素的顺序
        visited=[]
        order = []
        #由根节点开始深度图搜索
        def dfs(node):
            visited.append(node)
            order.append(node)
            for n in self.node_neighbors[node]:
                if not n in visited:
                    dfs(n)
        #先定义后引用
        if root:
            dfs(root)
        #返回访问元素顺序
        return order

    #广度优先搜索
    def breadthSearch(self,root=None):
        '''
        当队列不为空时，出队，(一般情况下会判断是否是要求元素，本例不再判断)
        如果不再被访问过的列表中，访问，放入被访问过的列表
        将该节点的邻节点入队
        '''
        #记载广度优先搜索的访问顺序
        visited=[]
        order=[]
        search_queue=deque()
        if root:
            search_queue+=self.node_neighbors[root]
            order.append(root)
            visited.append(root)
            while search_queue:
                #这种将整个列表中的元素入队只有在+=运算符下才可以
                node=search_queue.popleft()
                if not node in visited:
                    order.append(node)
                    visited.append(node)
                    search_queue+=self.node_neighbors[node]
        return order


if __name__=="__main__":
    g = Graph()
    g.add_nodes([i + 1 for i in range(8)])
    g.add_edge((1, 2))
    g.add_edge((1, 3))
    g.add_edge((2, 4))
    g.add_edge((2, 5))
    g.add_edge((4, 8))
    g.add_edge((5, 8))
    g.add_edge((3, 6))
    g.add_edge((3, 7))
    g.add_edge((6, 7))
    print(g.get_node_neighbors())

    print("广度优先：")
    print(g.breadthSearch(1))
    print("深度优先：")
    print(g.depth_first_search(1))


