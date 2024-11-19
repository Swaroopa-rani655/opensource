def mirr(matrix,n):
    for row in matrix:
        print(" ".join(map(str,row[::-1])))
n=int(input())
matrix=[]
for _ in range(n):
    row=list(map(int,input().strip().split()))
    matrix.append(row)
mirr(matrix,n)
