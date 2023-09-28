t=int(input())
for i in range(t):
    n=int(input())
    l1=input().split()
    l2=[]
    a=0
    b=0
    for i in range(n+1):
        if str(i) in l1:
            l2.append(i)
            l1.remove(str(i))
        else:
            a=i
            break
    l1.sort()
    for i in range(n+1):
        if str(i) in l1:
            pass
        else:
            b=int(i)
            break
    print(a+b)