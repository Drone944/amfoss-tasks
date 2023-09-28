import java.io.*;
import java.util.*;

public class Java
{
	public static void main(String[] args)
	{
		Scanner sc = new Scanner(System.in);
		int a;
		System.out.print("Enter the number : ");
		a = sc.nextInt();
		System.out.println();
		if((a==0)||(a==1))
		{
			System.out.println(a+" is neither a prime nor a composite number.");
		}
		else if(a==2)
		{
			System.out.println(a);
		}
		else
		{
			int c;
			for(int i=2;i<=a;i++)
			{
				c = 0;
				for(int j=2;j<a;j++)
				{
					if((i%j==0)&&(i!=j))
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
					System.out.println(i);
				}
			}
		}
	}
}