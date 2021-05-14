
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class CircularDoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next: #prevents infinite loop
                break


    def create(self, node_value):
        new_node = Node(node_value)
        self.head = new_node
        self.tail = new_node
        new_node.next = new_node
        new_node.prev = new_node


    def insert(self, value, location):
        if self.head is None:
            return 'the list does not exist'
        else:
            new_node = Node(value)
            if location == 0:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.head = new_node
                self.tail.next = new_node
            elif location == -1:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                new_node.next = temp_node.next
                new_node.prev = temp_node
                new_node.next.prev = new_node
                temp_node.next = new_node
                if temp_node == self.tail:
                    self.tail = new_node


    def traverse(self):
        if self.head is None:
            return 'there is no element in this list'
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                if temp_node == self.tail:
                    break
                temp_node = temp_node.next


    def reverse(self):
        if self.head is None:
            return 'there is no element in this list'
        else:
            temp_node = self.tail
            while self.tail:
                print(temp_node.value)
                if temp_node == self.head:
                    break
                temp_node = temp_node.prev


    def search(self, node_value):
        if self.head is None:
            return 'there is no element in this list'
        else:
            temp_node = self.head
            while temp_node:
                if temp_node.value == node_value:
                    return temp_node.value
                if temp_node == self.tail:
                    return 'the value does not exist in the list'
                temp_node = temp_node.next


    def delete(self, location):
        if self.head is None:
            return 'there is no node to delete'
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next 
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                cur_node = self.head
                index = 0
                while index < location - 1:
                    cur_node = cur_node.next
                    index += 1
                cur_node.next = cur_node.next.next
                cur_node.next.prev = cur_node

    
    def del_entire(self):
        if self.head is None:
            return 'there is nothing to delete'
        else:
            self.tail.next = None
            temp_node = self.head
            while temp_node:
                temp_node.prev = None
                temp_node = temp_node.next
            self.head = None
            self.tail = None





circularDLL = CircularDoubleLinkedList()
circularDLL.create(5)
circularDLL.insert(0, 0)
circularDLL.insert(3, 1)
circularDLL.insert(1, -1)
circularDLL.insert(2, 2)
# circularDLL.traverse()
# circularDLL.reverse()
# print(circularDLL.search(3))
# print([node.value for node in circularDLL])
# circularDLL.delete(2)
circularDLL.del_entire()
print([node.value for node in circularDLL])