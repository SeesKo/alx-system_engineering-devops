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
	pid_t child_pid;
	int i;

	/* Creating 5 child processes */
	for (i = 0; i < 5; i++)
	{
		/* Forking the process to create a child */
		child_pid = fork();

		/* Checking for fork errors */
		if (child_pid == -1)
		{
			perror("fork error");
			exit(EXIT_FAILURE);
		}

		/* Child process */
		if (child_pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}

	/* Parent process enters infinite loop */
	infinite_while();

	return (0);
}
