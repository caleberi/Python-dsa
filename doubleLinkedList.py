class Node(object):
    def __init__(self,value):
        self.info =  value
        self.prev = None
        self.next =  None


class DoubleLinkedList(object):
    def __init__(self):
        self.start = None

    def display_list(self):
        if self.start is None:
            print("List is empty")
            return

        print("List is : ")
        p = self.start
        while p is not None:
            print(p.info," ",end='')
            p = p.next
        print()


    def insert_in_begining(self,data):
        temp = Node(data)
        temp.next = self.start
        self.start.prev = temp
        self.start = temp

    def insert_in_empty(self,data):
        temp = Node(data)
        self.start = temp


    def insert_at_end(self,data):
        temp = Node(data)
        p = self.start
        while p.next is not None:
            p = p.next
        p.next =  temp
        temp.prev = p

    def create_list(self,data):
        self.insert_in_empty(data)
        for i in range(n-1):
            data = int(input("data:=>"))
            self.insert_at_end(data)

    def insert_after(self,data,x):
        temp = Node(data)
        p = self.start
        while p is not None:
            if p.info == x:
                break
            p = p.next
        if p is None:
            print(x," not present in the list")
        else:
            temp.prev = p
            temp.next = p.next
            if p.next is not None:
                p.next.prev = temp # should not be done when p refers to last Node
            p.next  = temp


    def insert_before(self,data,x):
        if self.start is None:
            print("List is empty")
            return
        if self.start.info == x:
            temp = Node(data)
            temp.next = self.start
            self.start.prev = temp
            self.start = temp
            return

        p = self.start
        while p is not None:
            if p.info == x:
                break
            p = p.next
        if p is None:
            print(x," not present in the list")
        else:
            temp = Node(data)
            temp.prev = p.prev
            temp.next = p
            p.prev.next = temp
            p.prev = temp

    def delete_first_node(self):
        if self.start is None: # list is empty
            return
        if self.start.next is None: #list has only one node
            self.start = None
            return
        self.start = self.start.next
        self.start.prev = None

    def delete_last_node(self):
        if self.start is None: # list is empty
            return
        if self.start.next is None: #list has only one node
            self.start = None
            return
        p = self.start
        while p.next != None:
            p = p.next
        p.prev.next = None

    def delete_node(self,x):
        if self.start is None: # list is empty
            return
        if self.start.next is None: #list has only one node
            if self.start.info == x:
                self.start = None
            else:
                print(x," not found")
            return
        if self.start.info == x:
            self.start = self.start.next
            self.start.prev = None
            return

        p = self.start.next
        while p.next is not None:
            if p.info == x:
                break
            p = p.next

        if p.next is not None: #nde to be deleted is in between
            p.prev.next = p.next
            p.next.prev = p.prev
        else: # p refers to the last Node
            if p.info  == x :# node to beg deleted is last Node
                p.prev.next = None
            else:
                print(x," not found")

    def reverse_list(self):
        if self.start is None: # list is empty
            return

        p1 = self.start
        p2 = p1.next
        p1.next  = None
        p1.prev = p2
        while p2 is not None:
            p2.prev = p2.next
            p2.next =  p1
            p1 = p2
            p2 = p2.prev
        self.start = p1p1


list = DoubleLinkedList()
