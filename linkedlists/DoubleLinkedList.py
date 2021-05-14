
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    
    def create(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
    
    
    def insert(self, nodeValue, location):
        if self.head is None:
            return 'node cannot be inserted'
        else:
            new_node = Node(nodeValue)
            if location == 0:
                new_node.prev = None #because first node prev is head which = None
                new_node.next = self.head #head keeps value of the first node which is now the 2nd node
                self.head.prev = new_node #previous reference of first node back to our new node
                self.head = new_node
            elif location == -1:
                new_node.next = None
                new_node.prev = self.tail #tail stored the last node information
                self.tail.next = new_node #last nodes next reference set to new node, tails next reference
                                          #used to be the last node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                new_node.next = temp_node.next
                new_node.prev = temp_node #because we are inserting after temp node
                new_node.next.prev = new_node
                temp_node.next = new_node


    def traverse(self):
        if self.head is None:
            return 'there is no element to traverse'
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.next


    def reverse_traversal(self):
        if self.head is None:
            return 'there is no element to traverse'
        else:
            temp_node = self.tail
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.prev


    def search(self, node_value):
        if self.head is None:
            return 'there is no element in this list'
        else:
            temp_node = self.head
            while temp_node:
                if temp_node.value == node_value:
                    return temp_node.value
                temp_node = temp_node.next
            return f'this element({node_value}) does not exist in the list'


    def del_node(self, location):
        if self.head is None:
            return 'there is no element in this list'
        else:
            if location == 0:
                if self.head == self.tail: #this is the only node
                    self.head = None
                    self.tail = None 
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail: #this is the only node
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev #creates link between tail and node before the last node
                    self.tail.next = None
            else:
                cur_node = self.head
                index = 0
                while index < location - 1:
                    cur_node = cur_node.next
                    index += 1
                cur_node.next = cur_node.next.next #gives us location of the node after current node
                cur_node.next.prev = cur_node #creates the reverse link back to cur node


    def del_list(self):
        if self.head is None:
            return 'there is not a list to delete'
        else:
            temp_node = self.head
            while temp_node:
                temp_node.prev = None 
                temp_node = temp_node.next
            self.head = None
            self.tail = None

                
    

doubleLL = DoubleLinkedList()
doubleLL.create(5)
doubleLL.insert(0,0)
doubleLL.insert(2,-1)
doubleLL.insert(6,2)

print([node.value for node in doubleLL]) 
# doubleLL.traverse()
# doubleLL.reverse_traversal()
# print(doubleLL.search(66))
# doubleLL.del_node(2)
# doubleLL.del_list()
# print([node.value for node in doubleLL])