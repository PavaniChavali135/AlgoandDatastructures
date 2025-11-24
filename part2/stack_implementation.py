class Stack:
    def __init__(self):
        self.elements =[]
    
    def push(self,data):
        self.elements.append(data)
        print(f"appended :{data}")

    def pop(self):
        if len(self.elements)==0:
            print("stack is empty")
            return None
        item = self.elements.pop()
        return item
    
    def peek(self):
        if len(self.elements)==0:
            print("stack is empty")
            return None
        return self.elements[-1]
    
    def traverse(self):
        if len(self.elements)==0:
            print("stack is empty")
            return None
        
        for i in reversed(self.elements):
            print(i)



ss = Stack()
ss.push(7)
ss.push(52)
ss.push(27)
ss.push(34)
ss.push(100)

ss.traverse()

ss.pop()

ss.traverse()

top =ss.peek()
print(top)



    