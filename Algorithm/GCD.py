'''
欧几里得求最大公约数(Greatest Common Divisor (GCD))
'''

def Gcd(a,b):
    m=a
    n=b
    #在这里不用要求a>=b，因为如果b大于a后在经过求余运算后会自动交换位置
    while(n):
        rem=m%n
        m=n
        n=rem
    return m

#测试用例
if __name__=="__main__":
    print(Gcd(16364,32828))