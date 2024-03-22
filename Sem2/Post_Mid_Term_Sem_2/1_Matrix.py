# Matrix in Python

class matrix:
    def __init__(self,arr):
        self.arr=arr

    def check(self, m, n):
        return len(self.arr)==m*n
    
    def create(self, m, n):
        self.a=[]
        for i in range(m):
            ls=[]
            for j in range(n):
                ls.append(self.arr[i*n+j])
            self.a.append(ls)

    def display(self):
        for i in self.a:
            print(*i)

    # Edit 2nd
    def reshape(self, m, n):
        M=[]
        tmp = []
        for i in self.lst:
            tmp.append(i)
            if len(tmp) == n:
                M.append(tmp)
                tmp=[]
        return matrix(M)



lst = list(map(int,input().split()))
row, column = list(map(int,input().split()))
obj = matrix(lst)
print(obj.check(row, column))

if obj.check(row, column):
    obj.create(row, column)
    obj.display()
else:
    print("Invalid Dimensions")


