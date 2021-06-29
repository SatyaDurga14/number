#include<iostream>
using namespace std;
int main()
{
	int len;
	cout<<"enter the length of the array";
	cin>>len;
	int arr[len];
	cout<<" enter array elements"<<endl;
	for(int i=0;i<len;i++)
	{
		cin>>arr[i];
	}
	cout<<"print the arr elemennts"<<endl;
	for(int i=0;i<len;i++)
	{
		cout<<arr[i]<<" ";
	}
	int query,left,right;
	cout<<endl<<"enter how many queries u want"<<endl;
	cin>>query;
	while(query)
    {
    	int sum=0;
    	cout<<"enter the left and right position"<<endl;
    	cin>>left>>right;
    	for(int j=left;j<=right;j++)
    	{
    		sum=sum+arr[j];
     	}
     	cout<<"the sum is"<<sum<<endl;
		query--;
	}
	return 0;
}
