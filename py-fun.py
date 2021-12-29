'''def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d
res1,res2=add_sub(5,4)
print(res1,res2)
'''
'''n=int(input())
c=0
l=[]
i=1
while i<=n:
    if n%i==0:
        l.append(i)
    i=i+1

for i in l:
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count=count+1
    if(count!=2):
            c+=1
            
            
print(l)    
print(c)
'''

'''class Student:
    college="ADITYA"
    def __init__(self,roll,per):
        self.rollno=roll
        self.per=per
    def display(self):'''
'''n=int(input())
n1=n
sum=0
for i in range(1,n+1):
    print(i)
    if n%i==0:
        sum=sum+i
        print('sum',sum)
if sum==n1:
    print("True")
else:
    print("False")
        '''
#recursion
def fun(n):
    if n==0:
        return
    fun(n-1)
    print(n)

n=5
fun(5)
