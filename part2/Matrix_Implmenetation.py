class Matrix:
    def __init__(self, elements):
        self.matrix = elements
        self.rows = len(elements)
        self.colmns = len(elements[0]) 
    def traverse(self):
        if self.rows == 0 or self.colmns == 0:
            print("Matrix is empty")
            return
        for row in self.matrix:
            print(row)

    def insertrow(self, index, rows):
        if self.colmns > 0 and len(rows) != self.colmns:
            return

        if index <= self.rows:
            self.matrix.insert(index, rows)
            self.rows = self.rows + 1
            if self.colmns == 0 and len(rows) > 0:
                self.colmns = len(rows)
            print(f"Row inserted at index {index}.")
        
    
    def insertclmn(self, index, clmns):
        if len(clmns) != self.rows:
            print(f"Error: New column must have {self.rows} rows.")
            return
        
        if index <= self.colmns:
            for i in range(self.rows):
                self.matrix[i].insert(index, clmns[i])
            self.colmns = self.colmns + 1
            print(f"Column inserted at index {index}.")
        

    def deleterow(self, index):
        if index < self.rows:
            delrow = self.matrix.pop(index)
            self.rows = self.rows - 1
            print(f"Row deleted at index {index}.")
            
            if self.rows == 0:
                self.colmns = 0
            return delrow
        
        
    def delclmn(self, index):
        if index < self.colmns:
            for i in range(self.rows):
                self.matrix[i].pop(index)
            self.colmns = self.colmns - 1
            print(f"Column deleted at index {index}.")
        



matrix = [
    [5, 6, 7],
    [8, 9, 10]
]

M = Matrix(matrix)
M.traverse()


M.insertrow(2, [234, 235, 236]) 

M.traverse()

M.insertclmn(1, [10, 20, 30])

M.traverse()
