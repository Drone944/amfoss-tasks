t=int(input())
v=[]
sx=0
sy=0
sz=0
for i in range(t):
    a=input().split()
    v.append(a)
for i in range(t):
    sx+=int(v[i][0])
    sy+=int(v[i][1])
    sz+=int(v[i][2])
if sx==0 and sy==0 and sz==0:
    print("YES")
else:
    print("NO")