'''
冒泡排序
每次比较相邻的两个元素，每次将较小元素或者较大元素依次放到最后
时间复杂度O(n^2)
升序排列
'''

def bubbleSort(arr):
    for i in range(len(arr)-1):
        #标志位，当在冒泡一趟过程中没有进行过交换，说明原列表已经有序
        flag=True
        for j in range(len(arr)-1-i):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                flag=False
        if flag:
            return arr
    return arr

#测试用例
if __name__=="__main__":
    print(bubbleSort([5,4,3,2,1]))
    print(bubbleSort([23,5,6,712,2,34,7]))
    print(bubbleSort([1,2,3,4,5]))



