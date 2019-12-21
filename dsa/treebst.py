class Node:
    def __init__(self, val):
        self.value = val
        self.leftchild = None
        self.rightchild = None

    def insert(self,data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.leftchild:
                return self.leftchild.insert(data)
            else:
                self.leftchild = Node(data)
                return True
        else:
               if self.rightchild:
                    return self.rightchild.insert(data)
               else:
                    self.rightchild = Node(data)
                    return True

                
    def find(self, data):
        if(self.value == data):
            return True
        elif self.value > data:
            if self.leftchild:
                return self.leftchild.find(data)
            else:
                return False
        else:
            if self.rightchild:
                return self.rightchild.find(data)
            else:
                return False

    def getheight(self):
        if self.leftchild and self.rightchild:
            return 1+max(self.leftchild.getheight(),self.rightchild.getheight())
        elif self.leftchild:
            return 1+self.leftchild.getheight()
        elif self.rightchild:
            return 1+self.rightchild.getheight()
        else:
            return 1

    def preorder(self):
        if self:
            print(str(self.value))
            if self.leftchild:
                self.leftchild.preorder()
            if self.rightchild:
                self.rightchild.preorder()

    def postorder(self):
        if self:
            if self.leftchild:
                self.leftchild.postorder()
            if self.rightchild:
                self.rightchild.postorder()
            print(str(self.value))

    def inorder(self):
        if self:
            if self.leftchild:
                self.leftchild.postorder()
            print(str(self.value))
            if self.rightchild:
                self.rightchild.postorder()
            

        


class Tree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self,data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def getheight(self):
        if self.root:
            return self.root.getheight()
        else:
            return 0
        

    def preorder(self):
        print("preorder")
        self.root.preorder()
        

    def postorder(self):
        print("postorder")
        self.root.postorder()
        

    def inorder(self):
        print("inorder")
        self.root.inorder()


    def remove(self, data):
        if self.root is None:
            return False

        elif self.root.value == data:
            if self.root.leftchild is None and self.root.rightchild is None:
                self.root = None
            elif self.root.leftchild and self.root.rightchild is None:
                self.root = self.root.leftchild
            elif self.root.leftchild is None and self.root.rightchild:
                self.root = self.root.rightchild
            else:
                delnodeparent = self.root
                delnode = self.root.rightchild

            while delnode.leftchild:
                delnodeparent = delnode
                delnode = delnode.leftchild

            self.root.value = delnode.value
            if delnode.rightchild:
                if delnodeparent.value > delnode.value:
                    delnodeparent.leftchild = delnode.rightchild
                elif delnodeparent.value < delnode.value:
                    delnodeparent.rightchild = delnode.rightchild
            else:
                if delnodeparent.value < delnode.value:
                    delnodeparent.leftchild = None
                else:
                    delnodeparent.rightchild =None
            return True
        parent = None
        node = selft.root
        while node and node.value != data:
            parent = node
            if data < node.value:
                node = node.leftchild
            elif data > node.value:
                node = node.rightchild

        if node is None and node.value != data:
            return False
        elif node.leftchild is None and node.rightchild is None:
            if data < parent.value:
                parent.leftchild = None
            else:
                parent.rightchild = None
            return True

        elif node.leftchild and node.rightchild is None:
            if data < parent.value:
                parent.leftchild = node.leftchild
            else:
                parent.rightchild = node.leftchild

            return True
        
        elif node.leftchild is None and node.rightchild:
            if data < parent.value:
                parent.leftchild = node.rightchild
            else:
                parent.rightchild = node.righttchild

            return True

        else:
            delnodeparent = node
            delnode = node.rightchild
            while delnode.leftchild:
                delnodeparent = delnode
                denode = delnode.leftchild
            node.value = delnode.value

            if delnode.rightchild:
                if delnodeparent.value > delnode.value:
                    delnodeparent.leftchild = delnode.rightchild
                elif delnodeparent.value < delnode.value:
                    delnodeparent.rightchild = delnode.rightchild
            else:
                if delnodeparent.value < delnode.value:
                    delnodeparent.leftchild = None
                else:
                    delnodeparent.rightchild =None
        



bst = Tree()

bst.insert(10)
bst.insert(8)
bst.insert(15)
bst.preorder()
bst.postorder()
bst.inorder()
print(bst.find(8))
print(bst.getheight())
bst.remove(10)
bst.inorder()

        
    
