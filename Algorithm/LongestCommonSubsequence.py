'''
最长公共子序列：
寻找两个字符串中相同的字符，不需要字符紧邻

时间复杂度：O(m*n)
分别为两个字符串的长度

思路：
动态规划，在动态规划网格中从左往右遍历整个网格
下面这个核心步骤体现出动态规划思想
if (A[i] == B[j])
    buff[i][j] = buff[i-1][j-1] + 1;
else
    buff[i][j] = max(buff[i-1][j], buff[i][j-1]);

最长公共子序列不唯一
'''
import numpy as np
class LCS(object):
    def __init__(self,str1,str2):
        self.string1=str1
        self.string2=str2
        self.string1_len=len(str1)
        self.string2_len=len(str2)
        self.cell=np.zeros([self.string1_len,self.string2_len],dtype="i4")
        #这个二维列表用来存储转移方向
        self.flag=[[0 for i in range(self.string2_len)] for j in range(self.string1_len)]
        #存储最长子序列的列表
        self.subsequence=[]

    def lcs(self):
        for i in range(self.string1_len):
            for j in range(self.string2_len):
                #如果最后一个字符相等，则在除去该字符基础上求两个序列的最长子序列
                if self.string1[i]==self.string2[j]:
                    #考虑网格边缘
                    if i==0 or j==0:
                        self.cell[i][j]=1
                        self.flag[i][j] = "ok"
                    else:
                        self.cell[i][j]=self.cell[i-1][j-1]+1
                        self.flag[i][j]="ok"
                #如果最后一个字符不相等，则求两个序列分别各去掉一个字符后的最长子序列的较大值
                else:
                    if i==0 and j==0:
                        self.cell[i][j]=0
                    elif i==0:
                        self.cell[i][j]=self.cell[i][j-1]
                        self.flag[i][j]="left"
                    elif j==0:
                        self.cell[i][j]=self.cell[i-1][j]
                        self.flag[i][j]="up"
                    elif self.cell[i-1][j]>self.cell[i][j-1]:
                        self.cell[i][j]=self.cell[i-1][j]
                        self.flag[i][j]="up"
                    else:
                        self.cell[i][j]=self.cell[i][j-1]
                        self.flag[i][j] = "left"
    def get_route(self):
        #确保跟矩阵的序号对应上
        i=self.string1_len-1
        j=self.string2_len-1
        while i>=0 and j>=0:
            if self.flag[i][j]=="ok":
                self.subsequence.append(self.string1[i])
                i-=1
                j-=1
            if self.flag[i][j]=="up":
                i-=1
            if self.flag[i][j]=="left":
                j-=1
        self.subsequence.reverse()
        return self.subsequence

if __name__=="__main__":
    ha=LCS('ABCBDAB','BDCABA')
    # ha=LCS('abdfg', 'abcdfg')
    ha.lcs()
    print(ha.get_route())





