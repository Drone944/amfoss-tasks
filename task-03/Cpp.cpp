#include <iostream>
using namespace std;

int main()
{
	int a;
	cout << "Enter the number : ";
	cin >> a;
	if((a==1)||(a==0))
	{
		cout << a <<" is neither a prime nor a composite number.";
	}
	else if (a==2)
	{
		cout << a;
	}
	else
	{
		for(int i=2;i<=a;i++)
		{
			int c=0;
			for(int j=2;j<(a);j++)
			{
				if((i%j==0)&&(j!=i))
				{
					c=1;
					break;
				}
				else
				{
					c=2;
				}
			}
			if(c==2)
			{
				cout << i<<"\n";
			}
		}
	}
	return 0;
}