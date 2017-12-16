#include <iostream>

using namespace std;

int main()
{
	int n;
	cin>>n;

	for(int i = 0; i <= n; i++)
	{
		int counter = 0;
		int output = false;
		int no = i;

		while(no > 0)
		{
			int val = no % 2;
			if(val == 0)
				counter++;
			else
			{
				if(counter % 2)
				{
					output = true;
					break;
				}
				counter = 0;
			}
			no /= 2;
		}

		if(output or counter % 2)
			cout<<"0, ";
		else
			cout<<"1, ";
	}
	cout<<endl;
	return 0;
}