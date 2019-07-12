'''
快速排序
1.选择基准点
2.将列表分成两个子列表：小于基准点元素的列表和大于基准点列表的元素
3.对两个子列表分别进行快速排序
'''
import random
def quick_sort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot=random.choice(arr)
        pivot_index=arr.index(pivot)
        #所有小于基准值的元素组成的子列表
        i=0
        less=[]
        greater=[]
        while i<len(arr):
            #所有小于基准值的元素组成的列表
            if arr[i]<pivot and i!=pivot_index:
                less.append(arr[i])
            #所有大于基准值的元素组成的列表
            if arr[i]>=pivot and i!=pivot_index:
                greater.append(arr[i])
            i+=1
        #python中要list做加法
        return quick_sort(less)+[pivot]+quick_sort(greater)

#测试用例
if __name__=="__main__":
    print(quick_sort([2,1,5,5,8,9]))
    print(quick_sort([293,4,523,456,3,8,3,9]))
    print([2])