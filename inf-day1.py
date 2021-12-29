'''def fun1(n):
    for i in range(n):    #0 to 4
        print('chinni')
fun1(5)
'''

'''class Student:
    college="aditya"
    def __init__(self,rollno,per):
        self.roll=rollno
        self.per=per
    def display(self):
        print(self.roll,self.per,Student.college) #here we can access object also .but we can access with class name only
s1=Student(596,68.7)
s1.display()
'''
'''
3 types of variables
1.local
2.instance:-its changes person to person or object to object 
3.class/static
self represents instance variables it change to object to object

'''
m=int(input())
n=int(input())
l=[]
for i in range(m,n+1):
    rev=0
    print('m=',i)
    temp=i
    while i:
        rem=i%10
        rev=rev*10+rem
        i=i//10
    if temp==rev:
        print(temp)
        l.append(temp)
    

print(l)
    
