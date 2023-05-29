#include <stdio.h>

/**
 * main - entry point
 *
 *  Return: Always 0 for success
 *
 */

int main(void)
{
	long unsigned int factorial = 1;
	int num, n;

	printf("Enter a number you want to find a factorial for: ");
	scanf("%d", &n);

	for (num = n; num > 0; num--)
	{
		factorial *= num;
	}
	printf("%lu\n", factorial);

	return (0);
}
