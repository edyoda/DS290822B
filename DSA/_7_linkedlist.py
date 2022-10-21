class node:
    def __init__(self,data,link = None):
        self.data = data # element
        self.link = link # memory location

class linkedlist:
    def __init__(self,head=None):
        self.head = head

    def is_empty(self):
        if self.head is None:
            return True

    def append(self,data):
        new_node = node(data,self.head) # data - 10 , None - link
        self.head = new_node # data - 10 ----> 1001 - link

    def display(self):
        itr = self.head
        while itr:
            print(itr.data)   
            itr = itr.link    

    def size(self):
        count = 0
        itr = self.head
        while itr:
            count += 1            
            itr = itr.link
        return count

    def appendleft(self,element):
        if self.is_empty():
            self.head = node(element)
            return

        itr = self.head
        while itr.link:
            itr = itr.link
        itr.link = node(element)

    def insert(self,index,data):
        if index < 0 or index > self.size :
            raise Exception("Invalid Index Error")

        if index == 0:
            self.append(data)
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node1 = node(data,itr.link)
                itr.link = node1
            itr = itr.link
            count += 1

    def remove(self,index):
        if index < 0 or index > self.size() :
            raise Exception("Invalid Index Error")

        if index == 0:
            self.head = self.head.link
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.link = itr.link.link
            itr = itr.link
            count += 1





if __name__ == "__main__":
    obj = linkedlist()
    # obj.append(10)
    # obj.append(20)
    # obj.append(30)
    # obj.display()
    # print(obj.size())

    obj.appendleft(10)
    obj.appendleft(20)
    obj.appendleft(30)
    # obj.insert(2,100)
    obj.remove(1)
    obj.display()



