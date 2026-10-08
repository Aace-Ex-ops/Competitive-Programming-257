class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertfront(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertend(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def deletefront(self):
        if self.head == None:
            return
        current = self.head
        self.head = current.next

    def deleteend(self):
        if self.head == None:
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def show(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")



print("Welcome to the Linked List Program!")

linked_list = LinkedList()

flag = True
while flag:
    print("Choose an operation:")
    print("1. Insert at the front")
    print("2. Insert at the end")
    print("3. Delete from the front")
    print("4. Delete from the end")
    print("5. Show the list")
    print("6. Exit")
    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        data = int(input("Enter the data to insert at the front: "))
        linked_list.insertfront(data)
    elif choice == 2:
        data = int(input("Enter the data to insert at the end: "))
        linked_list.insertend(data)
    elif choice == 3:
        linked_list.deletefront()
    elif choice == 4:
        linked_list.deleteend()
    elif choice == 5:
        linked_list.show()
    elif choice == 6:
        flag = False
    else:
        print("Invalid choice. Please try again.")
