
class Queue:
    def __init__(self, max_size):
        self.items = max_size * [None]
        self.max_size = max_size
        self.start = -1
        self.top = -1

    
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)


    def is_full(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.max_size:
            return True
        else:
            return False


    def is_empty(self):
        if self.top == - 1:
            return True
        else:
            return False


    def enqueue(self, value):
        if self.is_full():
            return 'Queue is full'
        else:
            if self.top + 1 == self.max_size: #our top element is pointing to the last element 
                self.top = 0
            else:
                self.top += 1
                if self.start == -1: #inserting at beginning
                    self.start = 0
            self.items[self.top] = value


    def dequeue(self):
        if self.is_empty():
            return 'there is no elements in the list'
        else:
            first_element = self.items[self.start] #we know first element is always where start points too
            start = self.start
            if self.start == self.top: #if this is the only element
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.max_size:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None #after returning first element we need to ignore it, not delete it
            return first_element


    def peek(self):
        if self.is_empty():
            return 'there is no elements in the list'
        else:
            return self.items[self.start]


    def delete(self):
        self.items = self.max_size * [None]
        self.top = -1
        self.start = -1


queue = Queue(3)
queue.enqueue(0)
queue.enqueue(1)
queue.enqueue(2)
# print(queue.dequeue())
# print(queue.peek())
queue.delete()
print(queue)