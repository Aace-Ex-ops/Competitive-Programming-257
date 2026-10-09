class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root == None:
            self.root = Node(data)
            return
        current = self.root
        while True:
             if data < current.data:
                if current.left == None:
                    current.left = Node(data)
                    break
                else:
                    current = current.left
             else:
                if current.right == None:
                     current.right = Node(data)
                     break
                else:
                    current = current.right

    def dfs(self, node):
        if node is not None:
            self.dfs(node.left)
            print(node.data)
            self.dfs(node.right)

bst1 = BinaryTree()
bst1.insert(10)
bst1.insert(5)
bst1.insert(15)
bst1.insert(3)
bst1.dfs(bst1.root)