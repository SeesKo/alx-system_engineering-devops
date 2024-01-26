#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - Creates an infinite loop.
 *
 * Return: Always returns 0.
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
 * main - Entry point of the program.
 *
 * Return: Always returns 0.
 */
int main(void)
{
	pid_t zombie_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		/* Forking the process to create a child */
		zombie_pid = fork();

		/* Checking for fork errors */
		if (zombie_pid == -1)
		{
			perror("fork error");
			exit(EXIT_FAILURE);
		}

		/* Child process */
		if (zombie_pid == 0)
			exit(0);
		else
			printf("Zombie process created, PID: %d\n", zombie_pid);
	}

	/* Parent process enters an infinite loop */
	return (infinite_while());
}
