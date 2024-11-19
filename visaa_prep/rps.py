V,C=input().split()
if V==C:
    print("NULL")
elif (V=="R" and C=="S") or (V=="S" and C=="P") or (V=="P" and C=="R"):
    print("Vignesh")
else:
    print("Charan")
