x,y,z=map(int, input().split())
total_time=x*y
avail=2*24*60
if total_time <= avail:
    print("YES")
else:
    print("NO")
