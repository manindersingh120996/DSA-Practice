class Node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self,data):
        node = Node(data=data,next=self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        if llstr[-3:] == '-->':
            llstr = llstr[:-3]
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data=data, next=None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data=data,next=None)

    def insert_values(self,data_list):
        self.head = None

        for value in data_list:
            self.insert_at_end(value)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        print(count)
        return count
    
    def remove_at(self,index):
        if index<0 or index>self.get_length():
            raise Exception("Not a Valid Index")

        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self,index,data):
        if index<0 or index >self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_begining(data=data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data=data,next=itr.next)
                itr.next = node
                break
            
            itr = itr.next
            count += 1
    
    def remove_by_value(self,value):
        count = 0
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        
        iter = self.head
        
        while iter.next:
            if iter.next.data == value:
                iter.next = iter.next.next
                break
            iter = iter.next
                

    





if __name__ == '__main__':
    ll = LinkedList()
    # ll.insert_at_begining(5)
    # ll.insert_at_begining(89)
    # ll.insert_at_begining(23)
    # ll.insert_at_end(69)
    ll.insert_values(["maninder","orange","games","Riyadh"])
    ll.get_length()
    # ll.remove_at(2)
    ll.insert_at(0,"laptop")
    ll.insert_at(3,"What")
    ll.remove_by_value("games")
    ll.print()
