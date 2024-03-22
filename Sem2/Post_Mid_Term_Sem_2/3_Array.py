class array:
    def __init__(self, flatlst, r=0, c=0):
        self.lst = []
        self.r = r
        self.c = c
        if r != 0 and c !=0:
            M = []
            arow = []
            for i in flatlst:
                arow.append(i)
                if len(arow) == c:
                    M.append(arow)
                    arow = []
            self.lst = M # This is the nested list

         
        # Here, we will keep filling mugs of water(elements or column) in a bucket(list for one row)
        # till it gets filled. Once filled, we pour the bucket in well(Matrix)
    
    def __add__(self, other):
        if (self.r, self.c) == (other.r, other.c):      # 1
            M = eval(str([[0]*self.c]*self.r))
            
            for i in range(self.r):
                for j in range(self.c):
                    M[i][j] = self.lst[i][j] + other.lst[i][j]
                return array(M)
        
    def __sub__(self, other):
        if (self.r, self.c) == (other.r, other.c):
            for i in range(self.r):
                for j in range(self.c):
                    M[i][j] = self.lst[i][j] - other.lst[i][j]
                return array(M)
        else:
            print('Not compatible for addition')

    def disp_mat(self):
        for i in self.lst:
            print(*i)

    # 2
            
    def __mul__(self, other):
        if (self.r, self.c) == (other.r, other.c):
            M = eval(str([[0]*self.c]*self.r))
            for i in range(self.r):
                for j in range(self.c):
                    for k in range(self.c):
                        M[i][j] += self.lst[i][k] * self.lst[k][i]
            return array(M)
        else:
            print("Not compatible")
    
    def transpose(self):
        M = eval(str([[0]*self.c]*self.r))
        for i in range(self.r):
            for j in range(self.c):
                M[j][i] = self.lst[i][j]
        return array(M)
    
    def flatten(self):
        # flat = []
        # for i in self.r:
        #     for j in self.c:
        #         flat.append(self.lst[i][j])

        flat = [str(row) for row in self.lst]


    
# driver code
        
lst1 = list(map(eval, input().split()))
r1, c1 = tuple(map(int, input().split()))
arr1 = array(lst1, r1, c1)

lst2 = list(map(eval, input().split()))
r2, c2 = tuple(map(int, input().split()))
arr2 = array(lst2, r2, c2)

print("Our first matrix")
arr1.disp_mat()

print("Our second matrix")
arr2.disp_mat()

print("Transpose of first matrix")
arr1.transpose().disp_mat()

print("Transpose of second matrix")
arr2.transpose().disp_mat()

print("This is the sum of two matrices")
print(arr1 + arr2)

print("This is the difference of two matrices")
print(arr1 - arr2)

print("This is the multiplication of two matrices")
print(arr1 * arr2)







# flattened list, which is not nested
# We didn't make seperate lists for marking rows, we continuously typed the cells in order

# variable length argument = arbitrary argument 

#1
# M = [[0] * self.c] * self.r This will give [[0,0,0],[0,0,0]..] but won't help
# as change in one record will change other record as they are duplicates using multiplication.
# we will convert list into string then it will convert to eval => list
# deep copy
# Now, no problem, eval places the records in different memory places
# changes won't reflect on all records now:

#2
# This is meant for simply multiplying the elements
# def __mul__(self, other):
#     if (self.r, self.c) == (other.r, other.c):
#         M = eval(str([[0]*self.c]*self.r))
#         for i in range(self.r):
#             for j in range(self.c):
#                 M[i][j] = self.lst[i][j] * other.lst[i][j]
#         return array(M)
#     else:
#         print("Not compatible")
