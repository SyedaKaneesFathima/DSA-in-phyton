class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def enQueue(head,val):
    print(val,"inserted")
    newNode=Node(val)
    if head == None:
        return newNode
    tail = head
    while tail.next !=None:
        tail=tail.next
    tail.next=newNode
    return head

def deQueue(head):
    if head== None:
        print("Queue is empty")
        return None
    temp=head.next
    print(head.data)
    head.next=None
    return temp

def frontvalue(head):
    if head == None:
        print("Queue is empty")
        return 
    print(head.data)

def printQueue(head):
    if head==None:
        print("Queue is empty")
        return
    curr=head
    while curr !=None:
        print(curr.data,end=" ")
        curr=curr.next
    print()
    
def printIsQEmpty(head):
    if head==None:
        print("Queue is empty")
    else:
        print("Queue is not empty")
        
head=None
n=int(input().strip())
while n>0:
    word=list(map(int,input().split()))
    l= word[0]
    if l == 1:
        num = word[1]
        head=enQueue(head,num)
    elif l == 2:
        frontvalue(head)
    elif l == 3:
        head = deQueue(head)
    elif l == 4:
        printQueue(head)
    else:
        printIsQEmpty(head)
    n -=1 

#sample input:-
11
1 12
1 34
1 56
1 32
2
4
3
4
5
1 222
4

#sample output:-
12 inserted
34 inserted
56 inserted
32 inserted
12
12 34 56 32
12
34 56 32
Queue is not empty
222 inserted
34 56 32 222
