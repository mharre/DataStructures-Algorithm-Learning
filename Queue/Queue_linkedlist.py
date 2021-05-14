
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def __iter__(self):
        cur_node = self.head
        while cur_node:
            yield cur_node
            cur_node = cur_node.next


class Queue:
    def __init__(self):
        self.linkedlist = LinkedList()


    def __str__(self):
        values = [str(x) for x in self.linkedlist]
        return ' '.join(values)


    def enqueue(self, value):
        new_node = Node(value)
        if self.linkedlist.head == None: #no elemet in linked list
            self.linkedlist.head = new_node
            self.linkedlist.tail = new_node
        else:
            self.linkedlist.tail.next = new_node #we know that the next reference of the tail is the previous nodes next reference 
            self.linkedlist.tail = new_node


    def is_empty(self):
        if self.linkedlist.head == None:
            return True
        else:
            return False


    def dequeue(self):
        if self.is_empty():
            return 'there is no element in the queue'
        else:
            temp_node = self.linkedlist.head
            if self.linkedlist.head == self.linkedlist.tail: #this means we have only 1 node
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.next 
            return temp_node


    def peek(self):
        if self.is_empty():
            return 'there is no element in the queue'
        else:
            return self.linkedlist.head


    def delete(self):
        self.linkedlist.head = None
        self.linkedlist.tail = None

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
# queue.dequeue()
print(queue.peek())
print(queue)