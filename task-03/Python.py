print("Enter the no. : ",end='')
n=int(input())
l1 = [2]
c=0
if n == 1 or n == 0:
	print(n," is neither a prime number nor a composite number.")
else:
	print(2)
	for i in range(2,n+1):
		for j in l1:
			if i%j==0:
				c=1
				break
			else:
				c=2
		if c==2:
			print(i)
			l1.append(i)
