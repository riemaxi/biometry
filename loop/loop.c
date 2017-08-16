#include <time.h>
#include "transition.h"
#include <stdio.h>

void delay(long nanosec)
{
	struct timespec res;
	res.tv_sec = 0;
	res.tv_nsec = nanosec;
	clock_nanosleep(CLOCK_MONOTONIC, 0, &res, NULL);
}

int main()
{
	long time_constant = start();
	
	while(next())
	{
		for(long i=0; !compute(i); i++);

		delay(time_constant);
	}

	end();

	return status();
}
