n=int(input())
matrix=[list(map(int,input().split())) for _ in range(n)]
row=[0]*n
col=[0]*n
for i in range(n):
    for j in range(n):
        row[i]+=matrix[i][j]
        col[j]+=matrix[i][j]
result=[]
for i in range(n):
    result.append(row[i]+col[i])
print(" ".join(map(str,result)))
