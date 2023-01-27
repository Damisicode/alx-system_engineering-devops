#include <stdio.h>
#include <unistd.h>
#include <stdbool.h>

/**
 * main - 5 zombie processes
 * Return: Always 0
 */

int infinite_while(void);

int main(void)
{
	int i;

	for (i = 0; i < 5; i++)
	{
		if (fork() == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			return 0;
		}
		else
		{
			sleep(1);
		}
	}
	infinite_while();
}

int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}
