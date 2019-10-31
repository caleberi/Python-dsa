 class Node:
    def __init__(self,value):
        self.info = value
        self.link = None

class SingleLinkedList:
    def __init__(self):
        self.start = None

    def concatenation(self,list):
        if self.start is None:
            self.start = list.start
            return
        if list.start is None:
            return
        p = self.start
        while p.link is not None:
            p = p.link

        p.link =  list.start


    def length(self):
        p = self.start
        count = 0
        while p is not None:
            if(p.info):
                count += 1
            p = p.link
        return count

    def display_List(self):
        if self.start is None:
            print("List is empty")
            return
        else:
            print("List is : ")
            p = self.start
            while p is not None:
                print(p.info)
                p = p.link
            print("")

    def count_nodes(self):
        p = self.start
        n = 0
        while p is not None:
            n+=1
            p = p.link

        print("Length:",n)

    def search(self,x):
        position = 0
        p = self.start
        while p is not None:
            if p.info  == x:
                print(x, "is at position ",position)
                return True
            position+=1
            p = p.link
        else:
            print(x," not found in list")
            return False



    def insert_in_beginning(self,data):
        temp = Node(data)
        temp.link =self.start
        self.start = temp

    def insert_at_end(self,data):
        temp =  Node(data)
        if self.start is None:
            self.start = temp
            return
        p = self.start
        while p.link is not None:
            p = p.link
        p.link = temp


    def create_list(self,n=0):
        for i in range(n):
            data = int(input("data:=>"))
            self.insert_at_end(data)


    def insert_after(self,data,x):
        temp =  Node(data)
        p =  self.start
        while p is not None:
            if p.info == x:
                break
            p=p.link
        if p is None:
            print(x," not present in the list")
        else:
            temp = p.link
            p.link = temp

    def insert_before(self,data,x):
        temp =  Node(data)
        p =  self.start

        if p is None:
            print("List is empty")
            return

        if p.link.info == x:
            temp.link = p.link
            p.link = temp
            return

        while p.link is not None:
            if p.link.info == x:
                break
            p=p.link

        if p.link is None:
            print(x," not present in the list")
        else:
            temp.link = p.link
            p.link = temp
            return




    def insert_at_position(self,data,x):
        temp =  Node(data)
        if x == 0:
            temp.link = self.start
            self.start =  temp
            return

        p =  self.start
        i = 0

        while p is not None and  i<x-1:
            p = p.link
            i +=1

        if p is None:
            print("You can insert only upto position",i)
        else:
            temp.link = p.link
            p.link = temp

    def delete_node(self,x):

        if self.start is None:
            print("List is empty")
            return

        if self.start.info == x:
            self.start = self.start.link
            return

        p = self.start
        while p.link is not None:
            if p.link.info == x:
                break
            p = p.link;

        if p.link is None:
            print(x,"does not exist because the node is empty")
        else:
            p.link = p.link.link



    def delete_first_node(self):
        if self.start is None:
            return
        self.start = self.start.link

    def delete_last_node(self):
        if self.start is None:
            return

        if self.start.link is None:
            self.start = None
            return

        p = self.start
        while p.link.link is not None:
            p = p.link

        p.link = None

    def reverse_list(self):
        prev = None
        current = self.start

        while current is not None:
            next = current.link
            current.link = prev
            prev = current
            current = next
        self.start = prev



    def bubble_sort_exdata(self):
        end = None
        while end != self.start.link:
            p=self.start
            while p.link != end:
                q=p.link
                if p.info > q.info:
                    p.info,q.info = q.info,p.info
                p = p.link
            end = p

    def bubble_sort_exlinks(self):
        end = None
        while end != self.start.link:
            r = p = self.start
            while p.link != end:
                q = p.link
                if p.info > q.info:
                    p.link  =  q.link
                    q.link = p
                    if p!=self.start:
                        r.link = q
                    else:
                        self.start = q
                    p,q = q,p
                r = p
                p = p.link
            end = p

    def has_cycle(self):
        if self.find_cycle() is None;
            return False
        else:
            return True


    def find_cycle(self):
        if self.start is None or self.start.link is None:
            return None
        hare = self.start
        tortoise = self.start
        while hare is not None or hare.link is None:
            hare = hare.link
            tortoise = tortoise.link.link
            if hare == tortoise:
                return tortoise
        return None

    def remove_cycle(self):
        c = self.find_cycle()
        if c  is None:
            return
        print("Node at which the cycle was detected is",c.info)

        p = c
        q = c
        len_cycle = 0
        while True:
            len_cycle +=1
            q = q.link
            if p == q:
                break
        print("Length of cycle is ",len_cycle)

        len_rem_list = 0
        p = self.start
        while p!=q:
            p = p.link
            q = q.link

        print("Number of nodes not included in the cycle are: ",len_rem_list)
        length_list =  len_cycle + len_rem_list
        print("Length of the list is :",length_list)

        p = self.start
        for i in range(length_list-1):
            p = p.link
        p.link = None

    def insert_cycle(self,x):
        if self.start is None:
            return
        p =  self.start
        px =  None
        prev =  None

        while p is not None:
            if p.info  == x:
                px = p
            prev = p
            p = p.link

        if px is not None:
            prev.link = px
        else:
            print(x," not present in list")


    def merge(self,list2):
        mergedList  =  SingleLinkedList()
        mergedList.start = self._merge_two_list(self.start,list2.start)
        return mergedList

    def _divide_list(self,p):
        pass
    def _merge_two_list(self,p1,p2):
        if p1.info <= p2.info:
            node =  Node(p1.info)
            p1 = p1.link
        else:
            node =  Node(p2.info)
            p2 = p2.link

        pM =  node

        while p1 is not None and p2 is not None:
            if p1.info <= p2.info:
                pM.link =  Node(p1.info)
                p1 = p1.link
            else:
                pM.link =  Node(p2.info)
                p2 = p2.link
            pM = pM.link

        #if second list has finished and elements left in the first list
        while p1 is not None:
            pM.link = Node(p1.info)
            p1 = p1.link
            pM = pM.link

        #if first list has finished and elements left in the second list

        while p2 is not None:
            pM.link = Node(p2.info)
            p2 = p2.link
            pM = pM.link

        return node


    def mergev2(self,list2):
        mergedList  =  SingleLinkedList()
        mergedList.start = self._merge_list(self.start,list2.start)
        return mergedList

    def _merge_list(self,p1,p2):
        if p1.info <= p2.info:
            startNode =  p1
            p1 = p1.link
        else:
          startNode =  p2
          p2 = p1.link

        pM =  startNode

        while p1 is not None and p2 is not None:
            if p1.info <=  p2.info:
                pM.link =  p1
                pM = pM.link
                p1 =  p1.link
            else:
                pM.link = p2
                pM =  pM.link
                p2 = p2.link

        if  p1 is None:
            pM.link = p2
        else:
            pM.link = p1

        return startNode
    def merge_sort(self):
        self.start = self._merge_sort_rec(self.start)

    def _merge_sort_rec(self,listStart):
        #if the list is empty or has one element
        if listStart is None or listStart.link is not None:
            return listStart
        # if more than one element
        start1 = listStart
        start2 = self._divide_list(listStart)
        start1  = self._merge_sort_rec(start1)
        start2  = self._merge_sort_rec(start2)
        startM = self._merge_list(start1,start2)
        return startM


    def _divide_list(self,p):
        q = p.link.link
        while q is not None and q.link is not None:
            p =  p.link
            q =  q.link.link
        start2 = p.link
        p.link = None
        return start2
