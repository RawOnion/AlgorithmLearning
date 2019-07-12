'''
最长公共子串
字符串中的子串的字符是连续的
时间复杂度为O(m*n)
两个字符串的长度之积

思路：
采用动态规划，从第一个子串开始遍历第二个子串
如果相等就在左上角值的基础上加一
'''
import numpy as np
class LongestCommonSubstring(object):
    def __init__(self,str1,str2):
        self.string1=str1
        self.string2=str2
        #保存字符串的长度
        self.string1_len=len(str1)
        self.string2_len=len(str2)
        #动态规划网格,这里的string1必须放在行，后面依赖这里来找字符位置
        self.cell=np.zeros([self.string1_len,self.string2_len],dtype="i4")
        #存放最大子串
        self.substring=[]

    def compute_common_substring(self):
        for i in range(self.string1_len):
            for j in range(self.string2_len):
                if self.string1[i]==self.string2[j]:
                    if i==0 or j==0:
                        self.cell[i][j]=1
                        #self.substring.append(self.string1[i])
                    else:
                        #相邻的对角线的值代表着两个字符相邻
                        self.cell[i][j]=self.cell[i-1][j-1]+1
                #下面这句其实可以不用写，但是为了逻辑完整性，加上了这句话
                else:
                    self.cell[i][j]=0

        #考虑到有可能在cell[][]中有两个子串，要把最大的子串放进substring中
        #找到cell中最大值的索引元组，然后只取第一个值，行的索引
        i=int(np.where(self.cell==self.cell.max())[0])
        for k in range(self.cell.max()):
            #依照行的索引去string1中找字符
            self.substring.append(self.string1[i])
            i-=1
        self.substring.reverse()
        return self.substring

if __name__=="__main__":
    he=LongestCommonSubstring("hafo","fo")
    print(he.compute_common_substring())



