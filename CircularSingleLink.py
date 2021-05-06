
class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CircularSingleLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next 
            if node == self.tail.next:
                break
           
    def create_CSLL(self, node_value, location):
        node = Node(node_value)
        node.next = node #setting it to itself because it's our only node
        self.head = node
        self.tail = node

    def insert_CSLL(self, value, location):
        if self.head is None:
            return 'The head reference is None'
        else:
            new_node = Node(value)
            if location == 0: #if 0 we want to insert at beginning
                new_node.next = self.head #next equals the "next" reference that was in the head node
                self.head = new_node
                self.tail.next = new_node #must create link between last node -> new (because circularLL)
            elif location == -1:
                new_node.next = self.tail.next
                self.tail.next = new_node
                self.tail = new_node
            else: #inserting in the middle of the list
                temp_node = self.head #so we start at node 1
                index = 0
                while index < location - 1: #this means we want to insert before the location, hence -1
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node
                if temp_node == self.tail:
                    self.tail = new_node

    def traverse_CSLL(self):
        if self.head is None:
            return 'No element for traversal'
        else:
            temp_node = self.head
            while temp_node: #while the temp node exists we loop
                print(temp_node.value)
                temp_node = temp_node.next
                if temp_node == self.tail.next:
                    break

    def search_CSLL(self, node_value):
        if self.head is None:
            return 'There is not any node in this CSLL'
        else:
            temp_node = self.head
            while temp_node:
                if temp_node.value == node_value:
                    return temp_node.value
                temp_node = temp_node.next
                if temp_node == self.tail.next:
                    return 'the node does not exist in this list'

    def delete_node(self, location):
        if self.head is None:
            return 'there is no node in this list'
        else:
            if location == 0:
                if self.head == self.tail: #this means we have only 1 node in list
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = next_node.next
    
    # Delete entire circular sinlgy linked list
    def deleteEntireCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None

circular_SSL = CircularSingleLinkedList() 
circular_SSL.create_CSLL(0, 0)
circular_SSL.insert_CSLL(1, 1)
circular_SSL.insert_CSLL(2, 2)
circular_SSL.insert_CSLL(3, 3)
circular_SSL.insert_CSLL(4, 4)
circular_SSL.insert_CSLL(5, -1)
# circular_SSL.traverse_CSLL()
# print(circular_SSL.search_CSLL(44))
circular_SSL.delete_node(2)
print([node.value for node in circular_SSL])
