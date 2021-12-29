'''n=int(input())
num=0
while n:
    r=n%10
    num=(num*10)+r
    n=n//10
print(num)'''

#palindrone or not
'''num=int(input())
n1=num
rev=0
while num:
    r=num%10
    rev=(rev*10)+r
    num=num//10
if(n1==rev):
    print("palindrone")
else:
    print("not palindrone")'''

#lcm of a number

'''a=int(input())
b=int(input())
mul=1
i=2
if a<b:
    while i:
        if a%i==0 and b%i==0:
            mul=mul*i
            a//=i
            b//=i
            print("mul=",mul,"a",a ,"b=",b)
            print()
        elif(b==i):
            mul=mul*a*b
            break
        else:
            i+=1
else:
    while i:
        if a%i==0 and b%i==0:
             mul=mul*i
             a//=i
             b//=i
        elif(a==i):
            mul=mul*a*b
            break
        else:
            i+=1
            
        
print(mul)
'''

'''#gcd of 2 numbers
a=int(input())
b=int(input())
gcd=1
i=2
if a<b:
    while i:
        if a%i==0 and b%i==0:
            a//=i
            b//=i
            gcd*=i
        elif(b==i):
            break
        else:
            i+=1
else:
    while i:
        if a%i==0 and b%i==0:
            a//=i
            b//=i
            gcd*=i;
        elif(a==i):
            break
        else:
            i+=1
print(gcd)'''

#swap to numbers easily
'''m=3
n=5
m,n=n,m
print("m",m," ","n",n)
        '''

#list
'''a=[1,2,3,4,5]
for i in range(len(a)):  # 0 5
    print(i,a[i])'''
#or
'''a=[1,2,3,4]
for i in a:
    print(i)'''

#find the length of the list
'''a=list(map(int,input().split())) #user enters the input into the shell
len=0
for i in a:
    len+=1
print(len)'''

 #find the max element in the list
'''a=list(map(int,input().split()))
max=0
for i in a:
    if(i>max):
        max=i
print(max)'''

#enter the elements to the empty dictionary
'''a={}
print("enter the number of keys")
n=int(input())
for i in range(n):
    k=input()
    a[k]=list(map(int,input().split()))
print(a)    '''

a=[1,2,3,4,1,3,5,6,9]
b=set(a)
d={}
for i in b:
    d[i]=a.count(i)
print(d)

a=[1,2,3,4,5,6,2,4,3,45,6,7]
d={}
for i in range a:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
print(d)

                               
               
               
                  
               
    
        

    
