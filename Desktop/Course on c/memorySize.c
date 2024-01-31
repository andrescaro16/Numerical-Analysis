#include <stdio.h>

//Code for testing size of memory of variables.

int main(){
    int myInt;
    int testInt;
    float testFloat;
    double testDouble;
    char myChar;

    printf("%lu\n", sizeof(myInt)); // 4
    printf("%lu\n", sizeof(testInt)); // 4
    printf("%lu\n", sizeof(testFloat)); // 4
    printf("%lu\n", sizeof(testDouble)); // 8 
    printf("%lu\n", sizeof(myChar)); // 1
    //use size of to check the size in memory of the variable 
    return 0;





}


/*
NOTE FROM W3Schools
"that we use the %lu format specifer to print the result, instead of %d. It is because the compiler expects the sizeof operator to return a long unsigned int (%lu), instead of int (%d). On some computers it might work with %d, but it is safer to use %lu.

Why Should I Know the Size of Data Types?
Using the right data type for the right purpose will save memory and improve the performance of your program.

You will learn more about the sizeof operator later in this tutorial, and how to use it in different scenarios."

"https://www.w3schools.com/c/c_data_types_sizeof.php"



*/