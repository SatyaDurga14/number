# check prime or not


'''def isprime(num):
    if num==1:
        return False
    for i in range(2,(n//2)+1,1):
        if(n%i==0):
            return False
    return True
            
'''
#or
'''
from math import sqrt
def isprime(num):
    if num==1:
        return False
    sq=int(sqrt(num))    #here sqrt fun will gives the float pointing nymber so we are converting into int
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True

n=int(input())
if isprime(n):
    print("prime")
else:
    print("not prime")

'''
# find factors of a number
'''
from math import sqrt
def fact_count(num):
    if num==1:
        return 1
    fc=2
    sq=int(sqrt(num))
    for i in range(2,sq+1):
        if n%i==0:
            fc+=2
    if sq*sq==num:
        fc-=1
    return fc


n=int(input())
print(fact_count(n))
'''
#other than 1 and itself factor which is the 1st factor return that fact otherwise if no factors other than 1 and itself then return -1
'''
from math import sqrt
def fact_count(num):
    if num==1:
        return 1
    sq=int(sqrt(num))
    for i in range(2,sq+1):
        if n%i==0:
            return i
    return -1


n=int(input())
print(fact_count(n))
'''

#other 1 and itsef factor which is the last factor return that fact otherwise if no factors other than 1 and itself then return -1
'''from math import sqrt
def fact_count(num):
    if num==1:
        return 1
    sq=int(sqrt(num))
    for i in range(2,sq+1):
        if n%i==0:
            return n//i
    return -1


n=int(input())
print(fact_count(n))
'''




'''
from math import sqrt
def fact_count(num):
    if num==1:
        return 1
    sq=int(sqrt(num))
    for i in range(2,sq+1):
        if n%i==0:
            return [i,n//i]
    return -1


n=int(input())
print(*fact_count(n))   #here before function name we put the * then the displays element with space n=100 then the output is ex:-2 50

'''
'''#k th position factor
def kth_fact(num,k):
    l=[]
    for i in range(1,num+1):
        if num%i==0:
            l.append(i)
    
    return -1

n=int(input())
k=int(input())
print(*(kth_fact(n,k)))
'''
#next prime number for  the given input

'''
n=int(input())
if n%2==0:
    '''

#reverse
'''
n=int(input())
print(n==int(str(n)[::-1]))  
'''


"""
here first the number is converted into string then it reverse
after it converts into ineger
"""

#next palindrone number
'''
def reverse(n):
    rev=0
    while n:
        rem=n%10
        rev=rev*10+rem
        n//=10
    return rev


n=int(input())
if n==reverse(n):
    print(n)
else:
    i=1
    while True:
        if n+i==reverse(n+i):
            print(n+i)
            break
        i+=1
'''

#previous palindrone
'''
def reverse(n):
    rev=0
    while n:
        rem=n%10
        rev=rev*10+rem
        n//=10
    return rev


n=int(input())
if n==reverse(n):
    print(n)
else:
    i=1
    while True:
        if n-i==reverse(n-i):
            print(n-i)
            break
        i+=1
'''
#
'''
def reverse(n):
    rev=0
    while n:
        rem=n%10
        rev=rev*10+rem
        n//=10
    return rev


n=int(input())
if n==reverse(n):
    print(n)
else:
    i=1
    while True:
        if n+i==reverse(n+i):
            R=n+i
            break
        i+=1
    i=1
    while True:
        if n-i==reverse(n-i):
            L=n-i
            break
        i+=1
    if abs(n-R)>=abs(n-L):
        print(L)
    else:
        print(R)
    
'''
#fibonaciii series
'''
10
0 1 1 2 3 5 8 13 21 34
'''
'''
def series(n):
    a=0
    b=1
    if n==1:
        print(a,end=" ")
    else:
        print(a,b,end=" ")
    for i in range(3,n+1):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
    

n=int(input())
series(n)
'''
'''
def series(n):
    d=[0]*n
    if n==1:
        print(*d)
        return
    d[1]=1
    for i in range(2,n):
        d[i]=d[i-1]+d[i-2]
    print(*d)

n=int(input())
series(n)
'''

#lcm
'''
def lcm(a,b,t=2):
    if a<t or b<t:
        return a*b
    if a%t==0 and b%t==0:
        return t*lcm(a//t,b//t,t)
    else:
        return l*lcm(a,b,t+1)


a,b=map(int,input().split(' '))
res=lcm(a,b)
print(res)

'''
#gcd
'''def gcd(a,b):
    while b:
        if a>b:
            a,b=b,a
        b=b%a
    return a

'''
'''
def gcd(a,b):
    if b==0:
        return a
    if a>b:
        a,b=b,a
    return gcd(a,b%a)
        
a,b=map(int,input().split(' '))
res=gcd(a,b)
print(res)
'''

#using a list of elements find the lcm ,gcd of the given numbers
'''
def lcm(a,b,t=2):
    if a<t or b<t:
        return a*b
    if a%t==0 and b%t==0:
        return t*lcm(a//t,b//t,t)
    else:
        return l*lcm(a,b,t+1)

def gcd(a,b):
    if b==0:
        return a
    if a>b:
        a,b=b,a
    return gcd(a,b%a)


n=int(input())
data=list(map(int,input().split()))
res=data[0]
for i in data[1:]:
    res=gcd(res,1)
print(res)
'''


s=input()
d=s.split(',')
print(d)
num=''
num2=0
c=0
for i in range(0,len(d)):
    print("i=",i)
    if d[i]=='5':
        while True:
            num=num+d[i]
            i+=1
            if d[i]=='8':
                num=num+d[i]
                c+=1
                print("num=",num)
                break
            
        
    else:
        num2=num2+int(d[i])
        print("num2=",num2)
s=int(num)
print(s+num2)
    
        
        
