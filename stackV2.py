class EmptyStackError(Exception):
    pass

class StackFullError(Exception):
    pass

class Stack:
    def __init__(self,max_size=10):
        self.items = [None]*max_size
        self.count = 0

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == len(self.items)

    def is_full(self):
        return self.count == len(self.items)

    def push(self,value):
        if self.is_full():
            raise StackFullError("Stack is full,can't push")

        self.items[self.count] = value
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty,can't pop")

        x = self.items[self.count-1]
        self.items[self.count-1] = None
        self.count -=1
        return x

    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty,can't peek")

        return self.items[self.count -1]

    def display(self):
        print(self.items)


if __name__ =="__main__":
    l = Stack()
    l.is_empty()
    l.push(34)
    l.push("John")
    l.push("mickel")
    l.push(4)
    l.push(564)
    l.push(True)
    l.display()
    b=l.pop()
    print(b)
    k=l.peek()
    print(k)
    l.size()
    print(l)
    l.display()
