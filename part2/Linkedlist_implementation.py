class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None

    def insertionatstart(self,data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def insertionatlast(self,data):
        newnode = Node(data)
        if self.head is None:
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = newnode

    def deletenode(self,value):
        curr = self.head
        prev = None

        if curr is not None and curr.data == value:
            curr = None
            print(f"deleted node with value: {value}")
            return
        while curr is not None and curr.data!=value:
            prev = curr
            curr = curr.next
        if curr is None:
            print("node is not found")
        
        prev.next = curr.next
        curr = None
        print("deleted node {value}")

    def traverse(self):
        if self.head == None:
            print("list is empty")
            return
        
        curr = self.head
        while curr.next:
            print(f"{curr.data}->",end="")
            curr= curr.next
        print(curr.data)



LL = Linkedlist()   
LL.insertionatstart(52)
LL.insertionatlast(34)
LL.insertionatlast(27) 
LL.insertionatstart(7)
LL.insertionatlast(100)

LL.traverse()

LL.deletenode(34)

LL.traverse()




    

    