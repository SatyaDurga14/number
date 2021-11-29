#include <stdio.h>

int main() {
    // Write C code here
 int num,i,j,sum;
 printf("enter the number");
 scanf("%d",&num);
 for(i=1;i<=num;i++)
 {
     sum=0;
     for(j=1;j<=i;j++)
     {
         if(i%j==0)
         {
            sum=sum+j; 
         }
     }
     if(sum< (i*2))
     {
         printf("the numbers are %d \n",i);
     }
 }
    
    return 0;
}
