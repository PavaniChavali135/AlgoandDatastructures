class dynamicarrays:
    def __init__(self):
        self.elements = []
        self.length = len(self.elements)

    def insert(self,index,data):
        self.elements.insert(index,data)
        self.length = self.length +1
        print(f"appended value:{data}")

    def delete(self,index):
        if index<len(self.elements):
            deletedvalue = self.elements.pop(index)
            self.length = self.length-1
            print(f"deleted value:{deletedvalue}")
        

    def traverse(self):
        print(self.elements)

array = dynamicarrays()
array.insert(0,7)
array.insert(1,52)
array.insert(2,27)
array.insert(3,34)
array.insert(4,100)

array.traverse()

array.insert(2,200)

array.traverse()

array.delete(4)

array.traverse()




