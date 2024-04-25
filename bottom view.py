#    18 
#   15  20 
# 25 30 45 80
#Bottom view :-
class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 

def printBottemViewOfBinaryTree(root):
    result = []
 
    Q = [[root, 0]]
    store = dict()
    while len(Q) > 0:
        currPair = Q.pop(0)
        # [address, hd] 
        node = currPair[0]
        hd = currPair[1]
        store[hd] = node.data
 
        if node.left != None:
            Q.append([node.left, hd - 1])
 
        if node.right != None:
            Q.append([node.right, hd + 1])

 

 root = TreeNode(18)
# 2- establishing links between nodes 
root.left = obj2 
root.right = obj3 
 
obj2.left = obj4 
obj2.right = obj5 
 
obj3.left = obj6 
obj3.right = obj7
printBottemViewOfBinaryTree(root)

