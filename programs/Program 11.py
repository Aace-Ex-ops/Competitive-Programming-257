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

    def bfs(self, node):
        if node is None:
            return
        queue = [node]

        while queue:
            node = queue.pop(0)
            print(node.data, end=" ")

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

bst1 = BinaryTree()

while True:
    print("1. Insert")
    print("2. Display")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter data to insert: "))
        bst1.insert(data)
    elif choice == 2:
        bst1.dfs(bst1.root)
    elif choice == 3:
        break
    else:
        print("Invalid choice")