#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
/**
 * infinite_while - A function that creates an infinite loop
 * Return: Void
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - A function that creates 5 zombie processes
 * Return: void
 */

int main(void)
{
	pid_t child_pid;
	int a = 0;

	for (; a < 5; a++)
	{
		child_pid = fork();

		if (child_pid == 0)
		{
			exit(0);
		}
		else if (child_pid < 0)
		{
			perror("Fork failed");
			exit(1);
		}
		else
		{
			printf("Zombie process created, PID: %d\n", child_pid);
		}
	}
	infinite_while();
	return (0);
}
