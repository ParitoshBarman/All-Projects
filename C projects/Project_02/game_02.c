#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Welcome to Paritosh's Visual Studio

int snakWaterGun(char you, char computer)
{

    // return 1 if you win,  -1 if you loss and 0 if draw
    // Cndition for draw
    // case covered :
    // ss
    // gg
    // ww
    if (you == computer)
    {
        return 0;
    }
    // Non draw condition
    // case covered:
    // sg
    // gs
    // sw
    // ws
    // gw
    // wg

    if (you == 's' && computer == 'g')
    {
        return -1;
    }
    else if (you == 'g' && computer == 's')
    {
        return 1;
    }

    if (you == 's' && computer == 'w')
    {
        return 1;
    }
    else if (you == 'w' && computer == 's')
    {
        return -1;
    }

    if (you == 'g' && computer == 'w')
    {
        return -1;
    }
    else if (you == 'w' && computer == 'g')
    {
        return 1;
    }
}

int main()
{
    char you, computer;

    srand(time(0));
    int number = rand() % 100 + 1; // Genarate the random number between 1 to 100

    if (number < 33)
    {
        computer = 's';
    }
    else if (number > 33 && number < 66)
    {
        computer = 'w';
    }
    else
    {
        computer = 'g';
    }

    printf("Enter 's' for snake, 'w' for water  and  'g' for gun --> ");
    scanf("%c", you);

    int result = snakWaterGun(you, computer);

    if (result == 0)
    {
        printf("Game draw!\n");
    }
    else if (result == 1)
    {
        printf("You win!\n");
    }
    else{
        printf("You loss!\n");
    }

    printf("You chose %c and computer chose %c\n", you, computer);

    return 0;
}