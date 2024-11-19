t=int(input())
for _ in range(t):
    x,n=map(int,input().split())
    points=x//10
    score=points*n
    print(score)
