'''
选择排序
时间复杂度为O(n^2)
'''

#找到最小值
def findSmall(arr):
    smallest_value=arr[0]
    smallest_index=0
    for i in range(1,len(arr)):
        if arr[i]<smallest_value:
            smallest_value=arr[i]
            smallest_index=i
    return smallest_index


#选择排序
def selectionSort(arr):
    sorted_arr=[]
    i=0
    while i<len(arr):
        smallest_index=findSmall(arr)
        sorted_arr.append(arr.pop(smallest_index))
    return sorted_arr


#测试用例
if __name__ == '__main__':
    arr=[4, 2, -5, -1, 6, 3]
    print(selectionSort(arr))