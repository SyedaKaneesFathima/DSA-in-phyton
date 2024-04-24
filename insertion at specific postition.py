
#insertion at specfic position:-
class node:
   def _init_(self, data):
       self.data = data
       self.prev = None
       self.next = None
      
def findTail(head):
   if head == None:
       return None
   tail = head
   while tail.next != None:
       tail = tail.next
   return tail


def insertAtEnd(head, ele):
   newNode = node(ele)
   if head == None:
       return newNode
   tail = findTail(head)
   tail.next = newNode
   newNode.prev = tail
   return head


def insertAtBeginning(head, ele):
   newNode = node(ele)
   if head == None:
       return newNode
  
   newNode.next = head
   head.prev = newNode
   head = newNode
   return head


def printLeftToRight(head):
   curr = head
   while curr != None:
       print(curr.data, end = " ")
       curr = curr.next
   print()
  
def printRightToLeft(head):
   tail = findTail(head)
   while tail != None:
       print(tail.data, end = " ")
       tail = tail.prev
   print()
      
      
def insertAtSpecificPosition(head, index, ele):
   newNode = node(ele)
   prev = None
   curr = head
   pos = 1
  
   while pos != index:
       prev = curr
       curr = curr.next
       pos += 1
      
   if prev == None:
       newNode.next = head
       head.prev = newNode
       return newNode
  
   newNode.next = curr
   curr.prev = newNode
   prev.next = newNode
   newNode.prev = prev
   return head
  
n = int(input())
l = list(map(int, input().split()))
temp = list(map(int, input().split()))
index, newElement = temp[0],temp[1]

head = None
for ele in l:
   head = insertAtEnd(head, ele)
printLeftToRight(head)
printRightToLeft(head)
head = insertAtSpecificPosition(head, index, newElement)
printLeftToRight(head)
printRightToLeft(head)
