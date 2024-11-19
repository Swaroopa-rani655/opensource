n=int(input())
curr=1
for i in range(1,n+1):
    row=[str(curr+j) for j in range(i)]
    print(" ".join(row))
    curr+=i
