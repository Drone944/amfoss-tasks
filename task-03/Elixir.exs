defmodule Primenos do
  def tocheckprime(n) when n <= 1, do: false
  def tocheckprime(2), do: true
  def tocheckprime(n) do
    Enum.all?(2..n-1, fn x -> rem(n, x) != 0 end)
  end

  def loop1(n) do
  	Enum.filter(2..n, &tocheckprime/1)
  end
end

a = IO.gets("Enter the no. : ") |> String.trim()
n = String.to_integer(a)
if (n==1)||(n==0) do
	IO.puts("#{n} is neither a prime nor a composite number.")
else
	if n==2 do
		IO.puts(n)
	else
		p = Primenos.loop1(n)
		Enum.each(p, &IO.puts/1)
	end
end