puts "Enter the no. : "
n=gets.chomp.to_i
l1=[2]
c=0
if n==1 or n==0
	puts "#{n} is neither a prime number nor a composite number."
else
	puts "The prime no.s : "
	puts 2
	for i in 2..n do
		for j in l1 do
			if i%j==0
				c=1
				break
			else
				c=2
			end
		end
		if c==2
			puts i
			l1.append(i)
		end
	end
end
