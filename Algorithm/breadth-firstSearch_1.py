'''
广度优先搜索算法:
时间复杂度O(节点数+边数)

应用案例，查找好友中是否有芒果销售商
1.创建队列
2.队列不为空则出队
3.判断这个人是否销售商
4.是则结束算法，否则将这个人的所有邻居入队
5.回到第二步
'''

from collections import deque

#有向图网络拓扑结构
#用字典来抽象有向图网络拓扑结构
graph={}
graph["you"]=["alice","bob","claire"]
graph["bob"]=["anuj","peggy"]
graph["alice"]=["peggy"]
graph["claire"]=["thom","jonny"]
graph["anuj"]=[]
graph["peggy"]=[]
graph["thom"]=[]
graph["jonny"]=[]


def breadth_firstSearch(graph):
    search_queue=deque()
    #这种列表入队只有在+=运算符下可以
    search_queue+=graph["you"]
    #列表用于记录已经检查过的人
    searched=[]
    while search_queue:
        person=search_queue.popleft()
        if not person in searched:
            if is_seller(person):
                print("%s is seller"%person)
                return True
            else:
                search_queue+=graph[person]
                searched.append(person)
    return False



def is_seller(person):
    return person[-1]=="m"

#测试用例
if __name__=="__main__":
    print(breadth_firstSearch(graph))
