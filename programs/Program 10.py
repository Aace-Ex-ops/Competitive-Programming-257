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

    def insertpos(self, data, position):
        if self.head == None:
            return
        
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        
        for i in range(position-1):
            if current == None:
                return
            current = current.next

        if current == None:
            return

        new_node.next = current.next
        current.next = new_node

    def deletefront(self):
        if self.head == None:
            return
        current = self.head
        self.head = current.next

    def deleteend(self):
        if self.head == None:
            return
        if self.head.next == None:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def deletepos(self, position):
        if self.head == None:
            return

        if position == 0:
            self.head = self.head.next
            return

        current = self.head

        for i in range(position - 1):
            if current == None:
                return
            current = current.next

        if current == None or current.next == None:
            return

        current.next = current.next.next
    def search(self, data):
        if self.head == None:
            return
        position = 0
        current = self.head
        while current:
            if current.data == data:
                print(f"{data} found in the list in position {position}.")
                return
            current = current.next
            position += 1
        print(f"{data} not found in the list.")

    def reverse(self):
        if self.head == None:
            return
        prev = None
        current = self.head
        while(current!=None):
            front = current.next
            current.next = prev
            prev = current
            current = front
        self.head = prev

        new_current = self.head
        while new_current:
            print(new_current.data, end=" -> ")
            new_current = new_current.next
        print("None")

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
    print("3. Insert at the position")
    print("4. Delete at front")
    print("5. Delete from the end")
    print("6. Delete from the position")
    print("7. Search for an element")
    print("8. Reverse the list")
    print("9. Show the list")
    print("10. Exit")
    choice = int(input("Enter your choice (1-10): "))

    if choice == 1:
        data = int(input("Enter the data to insert at the front: "))
        linked_list.insertfront(data)
    elif choice == 2:
        data = int(input("Enter the data to insert at the end: "))
        linked_list.insertend(data)
    elif choice == 3:
        data = int(input("Enter the data to insert at position: "))
        position = int(input("Enter position to insert at: "))
        linked_list.insertpos(data,position)
    elif choice == 4:
        linked_list.deletefront()
    elif choice == 5:
        linked_list.deleteend()
    elif choice == 6:
        position = int(input("Enter position to delete from: "))
        linked_list.deletepos(position)
    elif choice == 7:
        data = int(input("Enter the data to search for: "))
        linked_list.search(data)
    elif choice == 8:
        linked_list.reverse()
    elif choice == 9:
        linked_list.show()
    elif choice == 10:
        flag = False
    else:
        print("Invalid choice. Please try again.")
