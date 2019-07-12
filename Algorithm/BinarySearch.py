'''
二分查找
1.输入是一个有序的列表
2.返回是item在list的位置
应用场景：
list中可以保存名字，利用二分查找从list中查找名字
'''
def binary_search(item,arr):
    low=0
    high=len(arr)-1
    while low<=high:
        #在python中int相加做除法可以得到float，因此这里用了向下取整除
        mid=(low+high)//2
        guess=arr[mid]
        if guess==item:
            return mid
        if guess<item:
            low=mid+1
        else:
            high=mid-1
    #如果列表中没有元素则返回None
    return None


#测试用例
if __name__=="__main__":
    my_list=[1,5,6,9,10,14,165]
    print(binary_search(5,my_list))