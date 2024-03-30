#include  <stdio.h>

int main()
{
    printf ("hello world\n");
    int a = 31;
    for (int i = 0; i < 31; i++)
    {
        if (a > 1) 
        {
            a=a%2;
            printf ("%d", a);
        }
        
    }
}