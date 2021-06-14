#include<iostream>
using namespace std;
#include<bits/stdc++.h>
int balancedNumber(int N)
	{
	    // code here
	    int n1=N,n2=N,rem;
	    int count=0;
	    while(N)
	    {
	        rem=N%10;
	        count=count+1;
	        N=N/10;
	    }
	    if(count%2==1)
	    {
	        count=count/2;
	          int l=0,r=0;
	        for(int i=0;i<count;i++)
	        {
	           n1=n1%10;
	           l=l+n1;
	           n1=n1/10;
	        }
	        for(int j=count+1;n2!=0;j++)
	        {
	           n2=n2%10;
	           r=r+n2;
	           n2=n2/10;
	        }
	        if(l==r)
	        {
	            return 1;
	        }
	    }
	    else
	    {
	        return 0;
	    }
}
int main()
{
    int N,res;
    cin>>N;
   res=balancedNumber(N);
    cout<<res;
}
