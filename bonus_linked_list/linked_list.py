# Write code for implementing a linked list below

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

# Example usage
linked_list = LinkedList()
linked_list.insert_at_beginning(1)
linked_list.insert_at_beginning(2)
linked_list.insert_at_beginning(3)
linked_list.print_list()