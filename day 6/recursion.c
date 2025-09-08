#include <stdio.h>

void my_func(long long int n)
{
    double array[40] = {0.0};
    printf("Call Number-%ld \n", n);
    my_func(n + 1);
}

int main()
{
    my_func(1);
}