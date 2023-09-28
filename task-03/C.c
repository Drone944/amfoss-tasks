#include<stdio.h>

int main()
{
	printf("Enter the number : ");
	int a;
	scanf("%d",&a);
	if ((a==0)||(a==1))
	{
		printf("%d is neither a prime nor a composite number.",a);
	}
	else if (a==2)
	{
		printf("%d",a);
	}
	else
	{
		for(int i=2;i<=a;i++)
		{
			int c=0;
			for(int j=2;j<a;j++)
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
				printf("\n%d",i);
			}
		}
	}
	return 0;
}