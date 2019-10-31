class Node:
    def __init__(self,value):
        self.info = value
        self.right_child =None
        self.left_child =None

class BinaryTree:
    def __init__(self):
        self.root = None

    def empty(self):
        return self.root == None

    def display(self):
        self._display(self.root,0)
        print()

    def _display(self,p,level):
        if p is None:
            return
        self._display(p.right_child,level+1)
        print()

        for i in range(level):
            print("  ",end='')
        print(p.info)
        self._display(p.left_child,level+1)

    def preorder(self):
        self._preorder(self.root)
        print()

    def _preorder(self,p):
        if p is None:
            return
        print(p.info," ",end='')
        self._preorder(p.left_child)
        self._preorder(p.right_child)

    def postorder(self):
        self._postorder(self.root)
        print()

    def _postorder(self,p):
        if p is None:
            return
        self._postorder(p.left_child)
        self._postorder(p.right_child)
        print(p.info," ",end='')


    def level_order(self):
        if self.root is None:
            print("Tree is empty")
            return
        qu = deque()
        qu.append(self.root)

        while len(qu) != 0 :
            p = qu.popleft()
            print(p.info ," " ,end='')
            if p.left_child is not None:
                qu.append(p.left_child)
            if p.right_child is not None:
                qu.append(p.right_child)


    def height(self):
        return self._height(self.root)

    def _height(self,p):
        if p is None:
            return 0
        hL = self._height(p.left_child)
        hR = self._height(p.left_child)

        if hL > hR :
            return  1 + hL
        else:
            return 1 + hR

    def create_tree(self):
        self.root =  Node('P')
        self.root.left_child = Node('Q')
        self.root.right_child  =  Node('R')
        self.root.left_child.left_child = Node('A')
        self.root.right_child.right_child = Node('B')
        self.root.right_child.left_child = Node('X')


bt  = BinaryTree()
bt.create_tree()

bt.display()
print()
