class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
      
      
def push(top, val):
    print(val, "inserted")
    newNode = Node(val)
    newNode.next = top
    return newNode


def topValue(top):
    if top == None:
        print("Stack is empty")
        return
    print(top.data)

    
def pop(top):
    if top == None:
        print("Stack is empty")
        return None
    print(top.data)
    temp = top.next
    top.next = None
    return temp


def printStack(top):
    if top == None:
        print("Stack is empty")
        return
  
    curr = top
    while curr != None:
        print(curr.data, end = " ")
        curr = curr.next
    print()

def printStackEmpty(top):
    if top == None:
        print("Stack is empty")
    else:
        print("Stack is not empty")

top = None
n = int(input().strip())
while n > 0:
    word = list(map(int, input().split()))
    l = word[0]
    if l == 1:
        num = word[1]
        top = push(top, num)
    elif l == 2:
        topValue(top)
    elif l == 3:
        top = pop(top)
    elif l == 4:
        printStack(top)
    else:
        printStackEmpty(top)
    n -= 1
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

#output:-
12 inserted
34 inserted
56 inserted
32 inserted
32
32 56 34 12
32
56 34 12
Stack is not empty
222 inserted
222 56 34 12
