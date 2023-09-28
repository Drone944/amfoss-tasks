s=input()
h="hello"
c=-1
f=0
b=False
for i in h:
    try:
        b=s.index(i,c+1)>c
    except:
        b=False
    if (i in s) and b:
        c=s.index(i,c+1)
    else:
        f=1
if f==0:
    print("YES")
else:
    print("NO")