t = int(input())
for z in range(t):
    n = int(input())
    l1 = list(map(int,input().split()))
    c = 0
    e = 1
    if n==1:
        print(0)
    else:
        for j in range(n*10):
            for k in range(1,n):
                if l1[k]==0:
                    c = -1
            if ((l1 == sorted(l1)) and (e != 1)) or (c == -1):
                print(c)
                break
            for i in range(n):
                try:
                    if l1[i]>=l1[i+1]:
                        l1[i]=l1[i]//2
                        c += 1
                except:
                    pass
            e = 0
            for i in range(n):
                try:
                    if l1[i]==l1[i+1]:
                        e = 1
                except:
                    pass