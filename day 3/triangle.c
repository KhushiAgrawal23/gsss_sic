#include <stdio.h>

void draw_triangle(int numberOfLines)
{
    for (int i = 1; i <= numberOfLines; i++)
    { // for each line
        for (int j = 1; j <= numberOfLines - i; j++)
        {
            putc(' ', stdout);
        }
        for (int k = 1; k <= 2 * i - 1; k++)
        {
            putc('*', stdout);
        }
        printf("\n");
    }
}

int main()
{
    int numberOfLines = 17;
    draw_triangle(numberOfLines);
    return 0;
}