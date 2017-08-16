#include <stdio.h>

#define MAX_COUNTER 1000
#define TIME_CONSTANT 1000L

int counter;

int start()
{
	counter = 0;
	
	return TIME_CONSTANT;
}

int status()
{
	return 0;
}

int next()
{
	printf("counter %d\n", counter);
	return counter < MAX_COUNTER;
}

void end()
{
	printf("stopped at %d with status %d\n",counter, status());
}

int compute(int i)
{
	counter += 1;

	return 1;
}
