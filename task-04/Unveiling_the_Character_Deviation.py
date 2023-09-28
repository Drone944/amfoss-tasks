t=int(input())
for i in range(t):
    a=input()
    b="amfoss"
    c=0
    for i in range(len(b)):
        if a[i]!=b[i]:
            c+=1
    print(c)