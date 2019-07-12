'''
递归求和，递归最重要的两点：
1.递归体，不断地调用自己
2.递归出口，不再调用自己
'''

def totalSum(arr):
    if len(arr)==0:
        return 0
    else:
        return arr[0]+totalSum(arr[1:])

def list_num(arr):
    if len(arr)==0:
        return 0
    else:
        return 1+list_num(arr[1:])


#测试用例
if __name__=="__main__":
    print(totalSum([1,2,3,43,4]))
    print(totalSum([]))
    print(totalSum([5]))

    print(list_num([]))
    print(list_num([1]))
    print(list_num([2,3]))
    print(list_num([2,3,4,54]))

