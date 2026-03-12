r1= int(input("enter number of rows of first matrix: "))
c1= int(input("enter number of columns of first matrix: "))
r2= int(input("enter number of rows of second matrix: "))
c2= int(input("enter number of columns of second matrix: "))
print("enter values of first matrix")
m1 = [[int(input(f'enter element of {i} row\'s {j} col\' value: ')) for j in range(c1)] for i in range(r1)]
print("enter values of second matrix")
m2 = [[int(input(f'enter element of {i} row\'s {j} col\' value: ')) for j in range(c2)] for i in range(r2)]
m3 =  [[0 for _ in range(c2)] for _ in range(r1)]

for i in range(r1):
    for j in range(c2):
        for k in range(c1):
            m3[i][j] += m1[i][k] * m2[k][j]
[[print(m3[i][j], end='') for i in range(len(m3[0]))] for j in range(len(m3))]

        