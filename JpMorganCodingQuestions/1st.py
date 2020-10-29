"""
A String is provided as input from console which consist of integer.Insert '*' if subsequent numbers are even and insert '-'
if subsequent term are odd
"""

l=[]
def number(num):
    num = str(num)
    for i in range(len(num)):
        if(i == len(num)-1):
            l.append(num[i])
            break
        if int(num[i])%2==0 and int(num[i+1]) % 2 ==0:
            l.append(num[i])
            l.append('*')
        elif(int(num[i])%2!=0 and int(num[i+1]) % 2 !=0):
            l.append(num[i])
            l.append('-')
        else:
            l.append(num[i])
n = 21462675756
n2=98676555533
number(n2)
print("".join(l))
            
