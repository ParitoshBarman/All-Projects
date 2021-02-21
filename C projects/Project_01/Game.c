#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Welcome to Paritosh's Visual Studio

int main()
{
    int number, guess, count_try = 0;
    srand(time(0));
    number = rand() % 10 + 1; // Genarate the random number between 1 to 10

    
    printf("Guess a number 1 to 10\n");

    // Keep running the loop untill the number is guess

    do
    {

        scanf("%d", &guess);

        if (guess > number)
        {
            printf("Lower number please\n");
            count_try++;
        }
        else if (guess < number)
        {
            printf("Higher number please\n");
            count_try++;
        }
        else
        {
            count_try++;
            printf("Hurry You guess the number (;__;) ****\n\n You %d time try to find the number \n\n", count_try);
        }

    } while (guess != number);

    
    return 0;
}