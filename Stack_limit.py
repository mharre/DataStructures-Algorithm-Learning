
class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.list = []


    def __str__(self):
        # values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)


    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False


    def is_full(self):
        if len(self.list) == self.max_size:
            return True
        else:
            return False  


    def push(self, value):
        if self.is_full():
            return 'The stack is full'
        else:
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


stack = Stack(4)
# print(stack.is_empty())
# print(stack.is_full())
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.pop()
print(stack.is_full())