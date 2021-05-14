
class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SingleLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next  #so we can print out list

    def insert_link_list(self, value, location):
        new_node = Node(value)
        if self.head is None: #if none we need to create reference to head / tail
            self.head = new_node
            self.tail = new_node
        else: 
            if location == 0: #if 0 this means we are inserting at the beginning of the list
                new_node.next = self.head #updating the next reference of this new node to the reference that
                                          #was in the head
                self.head = new_node #updating head with new node physical location
            elif location == -1: #insert at end by checking location param
                new_node.next = None  #we know next reference in single link list is tail (None)
                self.tail.next = new_node #update the before node next reference to this new node
                                          #old node before this one used to reference tail
                self.tail = new_node #update tail with this new node (so we know this is now last node--> tail)
            else: #we want to update somewhere inside the list
                temp_node = self.head #need to start at head to traverse down list
                index = 0 #so we know where we are in the nodes (start at 0)
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next #we know that next node will be the temp_node.next current value
                temp_node.next = new_node #we know current node is temp node, so we can insert
                new_node.next = next_node #new_node.next value = the next node
                if temp_node == self.tail:
                    self.tail = new_node

    #traverse 
    def traverse_list(self):
        if self.head is None:
            return 'list does not exist'
        else:
            node = self.head 
            while node is not None:
                print(node.value)
                node = node.next #print value then go to next node

    #searching
    def search_list(self, value):
        if self.head is None:
            print('list does not exist')
        else:
            node = self.head
            while node is not None:
                if node.value == value:
                    return node.value
                node = node.next
            return 'value does not exist in this list'

    #deletion of single node
    def delete_node(self, location):
        if self.head is None:
            return 'List does not exist'
        else: 
            if location == 0:
                if self.head == self.tail: #if both are referencing the same node it means there is only 1
                    self.head = None
                    self.tail = None #setting both to none deletes the 1 node in between
                else: 
                    self.head = self.head.next #we know head itself stores location of next node
            elif location == -1:
                if self.head == self.tail: #if both are referencing the same node it means there is only 1
                    self.head = None
                    self.tail = None #setting both to none deletes the 1 node in between
                else: 
                    node = self.head
                    while node is not None:
                        if node.next == self.tail: #if the node.next = tail then we know we are at the node 
                                                   # before the tail
                            break 
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    #we need to traverse till the node which is before the node that we want to delete
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next #we know next node is current node's reference
                temp_node.next = next_node.next 
                #we need to set current node reference to the node that is after next node to break the chain
    
    #delete entire linked list
    def delete_entire_list(self):
        if self.head is None:
            return 'list does not exist'
        else:
            self.head = None
            self.tail = None


single_link_list = SingleLinkedList()
single_link_list.insert_link_list(1, 1)
single_link_list.insert_link_list(2, 1)
single_link_list.insert_link_list(3, 1)
single_link_list.insert_link_list(4, 1)
single_link_list.insert_link_list(0, 0)
single_link_list.insert_link_list(0, -1)

print([node.value for node in single_link_list])
# single_link_list.traverse_list()
# print(single_link_list.search_list(2))
single_link_list.delete_entire_list()
print([node.value for node in single_link_list])