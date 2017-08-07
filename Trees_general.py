class node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
class tree:
    def __init__(self):
        self.root = None
        self.created = {}
    def add(self,parent,child,child_type):
        if len(self.created)==0:
            self.created[parent]=node(parent)
            self.root = self.created[parent]
        if parent not in self.created:
            x = node(parent)
            self.created[parent] = x
            parent = x
        else:
            parent=self.created[parent]
        num = child
        child = node(child)
        if child_type=='L':
            parent.left = child
            self.created[num] = child
        else:
            parent.right = child
            self.created[num] = child
def height(root):
    if root is None:
        return 0
    else:
        lheight = height(root.left)
        rheight = height(root.right)
        if lheight > rheight :
            return lheight+1
        else:
            return rheight+1
            

def dfs(root,key):
    h = height(root)
    for i in range(1, h+1):
        x=[]
        x=printGivenLevel(root, i,x)
        k=len(x)
        if key in x:
            l = x.index(key)
            if(x[k-l-1]=="none"):
                return -1
            else:
                return x[k-l-1]
        
        
def printGivenLevel(root , level,x):
    if root is None:
        x.append('none')
        return 
        
    if level == 1:
        x.append(root.data)
    elif level > 1 :
        printGivenLevel(root.left , level-1,x)
        printGivenLevel(root.right , level-1,x)
    return x


t1=tree()
x = input().split(' ')
n = int(x[0])
q = int(x[1])

for i  in range(n-1):
    y = input().split(' ')
    parent = int(y[0])
    child = int(y[1])
    child_type = y[2]
    t1.add(parent,child,child_type)


for j in range(q):
    qu=int(input())
    print(dfs(t1.root,qu))
    
    
  """
#input format 
<parent> <element> <type - left child/right child>
1 2 R
1 3 L
2 4 R
2 5 L
3 6 R
3 7 L
5 8 R
"""
5 9 L
7 10 R
