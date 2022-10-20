class node:
    def __init__(self,data,link=None):
        self.data = data
        self.link = link

class linkedlist:
    def __init__(self,head=None):
        self.head = head

    def is_empty(self):
        if self.head == None:
            return True
            
    def append(self,element):
        new_node = node(element)
        if self.is_empty:
            self.head = new_node
        else:
            temp = self.head
            while temp.link != None:
                temp = temp.link
            temp.link = new_node
        print("Node have been inserted")

    def display(self):
        pass



if __name__ == "__main__":
    obj = linkedlist()
    obj.append(10)
    obj.append(20)
    obj.append(30)

        


