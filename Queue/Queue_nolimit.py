
class Queue:
    def __init__(self):
        self.items = []

    
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)


    def is_empty(self):
        if self.items == []:
            return True
        else:
            return False


    def enqueue(self, value):
        self.items.append(value)


    def dequeue(self):
        if self.is_empty():
            return 'there is no element in the queue'
        else:
            return self.items.pop(0)


    def peek(self):
        if self.is_empty():
            return 'there is no element in the queue'
        else:
            return self.items[0]


    def delete(self):
        self.items = None


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.dequeue()
print(queue.peek())
# queue.delete()
print(queue)