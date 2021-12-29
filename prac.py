'''N=int(input())
X=int(input())
div1=1
for i in range(1,X+1,1):
    div1*=10
last2=N%div1
print(last2)
count=0
while N:
    N//=10
    count+=1
print("Number",count)
print(count-X+1)
div2=1
for i in range(1,count+1-X,1):
    div2*=10
first=N//div2
print("first",first)
    '''
    
a,b=map(int,input().split(' '))
i=2
lcm=1
while True:
    if (a%i==0 and b%i==0):
        lcm*=i
        a//=i
        b//=i
        print("l=",lcm,"a=",a,"b",b)
        if(a==1 or b==1):
            lcm=lcm*a*b
            break
    else:
        i+=1
print(lcm)


