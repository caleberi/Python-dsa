class Queue:
    def __init__(self):
        self.arr = []

    def is_empty(self):
        return len(self.arr) == 0

    def size(self):
        return len(self.arr)

    def enqueue(self,value):
        self.arr.append(value)

    def dequeue(self):
        if self.is_empty():
            raise EmptyStackError("Queue is empty")
        return self.arr.pop(0)

    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Queue is empty")
        return self.arr[0]


    def display(self):
        print(self.arr)


if __name__ =="__main__":
    q = Queue()
    q.enqueue(23)
    q.enqueue(34)
    q.enqueue(12)
    q.enqueue(19)
    q.enqueue(16)
    q.enqueue(112)
    q.display()
    q.dequeue()
    q.display()
