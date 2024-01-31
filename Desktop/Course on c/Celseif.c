#include <stdio.h>

//very simple code to try the else if arguments in c.


int main(){
    int numx;
    int numz;
 //dont forget that for scanf before the name of the variable you want to input there must be an & as seen below.
    printf("\n enter x:");
    scanf("%d",&numx); 
    printf("\n enter z:");
    scanf("%d",&numz);

//small note theres a shorter syntax for if else
//variable = (condition) ? expressionTrue : expressionFalse;

  

    if(numx > numz){
        printf("the sum of the two numbers is = %d",numx + numz);
       
    }
    else if (numx < numz){
        printf("the substraction of both numbers is = %d", numx - numz);
        
    
    }
    else{
        
        printf(" the number x must be greater than z: \n");
        printf("x is: %d\n", numx);
        printf("z is: %d\n", numz);

        
    }




}