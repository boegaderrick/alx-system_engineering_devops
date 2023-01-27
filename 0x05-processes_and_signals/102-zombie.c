#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

/**
 * infinite_while - sleeps infinitely
 * Return: 0
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
 * main - creates zombie processes
 * Return: 0
 */
int main(void)
{
	int i = 0, pid = 1;

	while (i < 5 && pid != 0)
	{
		pid = fork();
		if (pid != 0)
			printf("Zombie process created, PID: %d\n", pid);
		i++;
	}
	if (pid != 0)
		infinite_while();
	return (0);
}
