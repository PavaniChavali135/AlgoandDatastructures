class Queue:
    def __init__(self):
        self.elements =[]

    def enqueue(self, data):
        self.elements.append(data)

    def dequeue(self):
        if len(self.elements)==0:
            print("queue is empty")
        
        lastelement = self.elements.pop()
        print(f"popped element:{lastelement}")

    def traverse(self):
        print(self.elements)
              
    
q = Queue()

q.enqueue(7)
q.enqueue(52)
q.enqueue(27)
q.enqueue(34)
q.enqueue(100)

q.traverse()

q.dequeue()

q.traverse()



    