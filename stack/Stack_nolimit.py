#creating a stack w/ no size limit
class Stack:
    def __init__(self):
        self.list = [] #creating our empty stack


    def __str__(self):
        # values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values) #simply prints out the list in a 'stack format' meaning ontop of eachother


    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False


    def push(self, value):
        self.list.append(value)


    def pop(self):
        if self.is_empty():
            return 'There are no elements in the stack'
        else:
            return self.list.pop()


    def peek(self):
        if self.is_empty():
            return 'There are no elements in the stack'
        else:
            # return self.list[len(self.list)-1]
            return self.list[-1]


    def delete(self):
        self.list = None

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())
print(stack.delete())