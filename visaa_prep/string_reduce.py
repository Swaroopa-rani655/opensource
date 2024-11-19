def re_string(s):
    result=[]
    n=len(s)
    if n==0:
        return ""
    count = 1
    for i in range(1,n):
        if s[i]==s[i-1]:
            count+=1
        else:
            result.append(s[i-1] + (str(count)))
            count=1
    result.append(s[-1] + (str(count)))
    return ''.join(result)
input_string=input().strip()
print(re_string(input_string))
