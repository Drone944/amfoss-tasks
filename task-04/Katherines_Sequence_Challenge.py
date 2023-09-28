t = int(input())
for i in range(t):
    n = int(input())
    l1 = []
    f1 = []
    x = 0
    a = 0
    b = -1
    c = -1
    s = ''
    for i in range(n):
        l1.append(list(map(int,input().split())))
    for j in range(n-1):
        l2=[]
        for z in range(n):
            l2.append(l1[z][j])
        for k in range(n):
            if l2.count(l2[k])>len(l2)//2:
                a = l2[k]
            if l2.count(l2[k])<len(l2)//2:
                x = l2[k]
        for m in range(len(l2)):
            if (l2.count(l2[m])==len(l2)//2) and (l2[m]==x):
                b = l2[m]
            if (l2.count(l2[m])==len(l2)//2) and (l2[m]!=x):
                c = l2[m]
        if a not in f1:
            f1.append(a)
        if b not in f1 and b != -1:
            f1.append(b)
        if c not in f1 and c != -1:
            f1.append(c)
    for q in range(len(f1)):
        print(f1[q],end=' ')
    print()