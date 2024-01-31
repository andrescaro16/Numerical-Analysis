#include <stdio.h>

int main(){

    float div = 5 / 2;
    printf("%f\n", div); //output of this would still be 2 therfore we need to manually convert the integer values to float values
    
    float div2 = (float) 5/2;
    printf("%f\n", div2); // result = 2.500000

    int a = 5;
    int b = 2;
    float div3 = (float) a/b; // another way as seen before but this time with a and b as int values converted to float values.
    printf("%.2f", div3); //rounded to two decimal places.

}

/* Notes. its important to realize that c automatically converts int to float and vice versa 
i.e. when you asigned a float to an int as in int a = 9.99 the output would be 9 and if you 
asigned a int to a float like float b = 9 the output would be 9.000000 */
