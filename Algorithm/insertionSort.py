'''
插入排序（正序排序）
在原列表上直接进行排序
时间复杂度为O(n^2)
'''

def insertionSort(arr):
    for i in range(len(arr)):
        x=arr[i]
        for j in range(i,-1,-1):
            if j==0:
                break
            #j-1是试探位置
            if x<arr[j-1]:
                arr[j]=arr[j-1]
            else:
                break
        arr[j]=x
    return arr

#测试用例
if __name__=="__main__":
    print(insertionSort([2,3,4,51,3,323,4]))
    print(insertionSort([1]))
    print(insertionSort([2,2,2,5,1,7,89]))