'''
class Node:
    def __inti__(self,val):
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        
        


l1=LinkedList([1,4,9,16])

'''
n=int(input())
data=list(map(int,input().split()))
dic={}
for i in data:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for k in dic.keys():
    print(k,end=" ")


n=int(input())
data=list(map(int,input().split()))
data.sort(reverse=True)
dic={}
for i in data:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for k in dic.keys():
    print(k,end=" ")
