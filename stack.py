class  EmptyStackError(Exception):
    pass

class Stack:
    def  __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise EmptyStackError("stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise EmptyStackError("stack is empty")
        return self.items[-1]

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
