#include <stdio.h>
#include <stdlib.h>
int main(int argc, char *argv[]) {
    int value = atoi(argv[1]);
    value += 10;
    if (value == 'Z')
	    printf("Win\n");
    else 
	    printf("False\n");
    return 0;
}
