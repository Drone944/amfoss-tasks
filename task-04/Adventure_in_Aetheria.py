n=int(input())
b=[]
a=input().split()
for i in a:
    b.append(int(i))   
m=min(b)
if b.count(m)>1:
    print("Still Aetheria")
else:
    print(b.index(m) + 1)