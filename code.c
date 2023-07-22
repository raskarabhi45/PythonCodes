#include<stdio.h>
int insert(int[],int);
void Display();

int main()
{
    int arr[100],n=0;
    printf("enter size\n");
    scanf("%d",&n);

    for(int i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }

    for(int i=0;i<n;i++)
    {
        printf("%d\t",arr[i]);
    }

    n=insert(arr,n);
    Display(arr,n);

    return 0;
}

int insert(int arr[],int n)
{
    int i,pos,val;
    printf("\nEnter position and value\n");
    scanf("%d %d",&pos,&val);
    for(i=n-1;i>=pos-1;i--)
    {
        arr[i+1]=arr[i];
    }
    arr[pos-1]=val;

    return n+1;
}

void Display(int arr[],int n)
{
    int i;
    for(i=0;i<n;i++)
    {
        printf("%d\t",arr[i]);
    }
}