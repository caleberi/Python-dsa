class Node:
    def __init__(self,value):
        self.info = value
        self.link = None

class EmptyStackError(Exception):
    pass

class Stack:
    def __init__(self):
         54ea
        self.top = None
        self.length = 0

    def push(self,data):
        temp = Node(data)
        temp.link =self.top
        self.top = temp
        self.length +=1

    def pop(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        popped_data = self.top.info
        self.top = self.top.link
        self.length -=1
        return popped_data

    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")

        return self.top.info

    def is_empty(self):
        return self.length == 0

    def size(self):
        return self.length

    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        else:
            print("Stack is : ")
            p = self.top
            while p is not None:
                print(p.info)
                p = p.link
            print("")

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
    print("=============>")
    b=l.pop()
    print(b)
    print("=============>")
    k=l.peek()
    print(k)
    print("=============>")
    l.size()
    print("=============>")
    l.display()
