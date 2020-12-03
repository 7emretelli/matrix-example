#####################
###Coded By##########
#####Emre##Telli#####
#####################

m = int(input("m"))  # m is row of A
n = int(input("n"))  # n is column of A and row of B
p = int(input("p"))  # p is column of B


A = [1, 2, 3, 4, 5, 6]
B = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]


def matrixCreator(array, column, row):
    numbersofarray = column * row

    arraynum = 0
    for i in range(row):
        for r in range(column):
            print(array[arraynum], end=" ")
            arraynum += 1
        print("\n")


def matrixArrayCreator(array, column, row):
    numbersofarray = column * row
    arraynum = 0
    matrixarray = []
    for i in range(row):
        row = []
        for r in range(column):
            row.append(array[arraynum])
            arraynum += 1
        matrixarray.append(row)
    return(matrixarray)


print("matrix A")
matrixCreator(A, n, m)
print("matrix B")
matrixCreator(B, p, n)

a = matrixArrayCreator(A, n, m)
b = matrixArrayCreator(B, p, n)


print("Matrix Product:")
result = [[sum(a * b for a, b in zip(A_row, B_col))
           for B_col in zip(*b)]
          for A_row in a]

for r in result:
    print(r)
