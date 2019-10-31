class Node(object):
    def __init__(self,value):
        self.info = value
        self.link = None

class CircularLinkedList(self):
    def __init__(self):
        self.last = None

    def display_list(self):
        if self.last == None:
            print("List is empty\n")
            return

        p = self.last.link

        while True:
            print(p.info," ",end='')
            p = p.link
            if p == self.last.link:
                break
        print()

    def insert_in_begining(self,data):
        temp = Node(data)
        temp.link =self.last.link
        self.last.link = temp

    def insert_in_empty(self,data):
        temp =  Node(data)
        self.last = temp
        self.last.link = self.last

    def insert_at_end(self,data):
        temp =  Node(data)
        temp.link =  self.last.link
        self.last.link = temp

    def insert_after(self,data,x):
        pass

    def delete_only_node(self):
        self.last = None

    def delete_first_node(self):
         if self.last is None: # list is empty
            return
        if self.last.link == self.last: # has only one Node
            self.last = None
            return
        self.last.link =  self.last.link.link

    def delete_last_node(self):
        if self.last is None: # list is empty
           return

        if self.last.link == self.last: # has only one Node
           self.last = None
           return

       p = self.last.link
       while p.link != self.last:
           p = p.link
       p.link =  self.last.link
       self.last = p

   def delete_node(self,x):
       if self.last is None: # list is empty
          return

       if self.last.link == self.last and self.last.info == x: # has only one Node
          self.last = None
          return

      if self.last.link.info  == x: #deletion of first node
          self.last.link = self.last.link.link
          return

      p =  self.last.link
      while p.link != self.last.link:
          if p.link.info == x:
              break
          p = p.link

     if p.link == self.last.link:
         print(x," not found in the list ")
     else:
         p.link = p.link.link
         if self.last.info == x:
             self.last = p
