#include <stdio.h>
#include <stdbool.h>   // we need to include the stdbool library as bool isnt built in c.


int main(){
    bool HamburguersAretasty = true;
    bool iLikeHamburguers = true;
    bool iLikeCola = false;
    printf("%d\n",iLikeCola);   //bool values are returned as 1 or 0 so we must use the format specifier %d for integers!
    printf("%d\n",HamburguersAretasty);
    printf("%d\n", iLikeCola == HamburguersAretasty);
    printf("%d\n",HamburguersAretasty == iLikeHamburguers);

    //we can use operators to compare operations like:

    printf("%d\n",10>9);
    printf("%d\n",0>9);
    printf("%d\n",10==10);

    printf("%d\n","hello"=="hello");
    return 0;


}