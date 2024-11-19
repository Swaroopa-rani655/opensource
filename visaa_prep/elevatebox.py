n=int(input())
a=list(map(int,input().split()))
tot=sum(a)
left_sum=0
bal_arr=[]
for i in range(n):
    right_sum=tot - left_sum - a[i]
    bal=abs(left_sum - right_sum)
    bal_arr.append(bal)
    left_sum += a[i]
print(" ".join(map(str,bal_arr)))
