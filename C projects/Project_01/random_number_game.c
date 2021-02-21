#include<stdio.h>
#include<stdlib.h>
#include<time.h>


 
 // Welcome to Paritosh's Visual Studio


int main(){
    int number ;
    srand(time(0));
    number= rand()%10 + 1 ; // Genarate the random number between 1 to 100

    printf("The number is %d\n",number);





    return 0;
}