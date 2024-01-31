#include <stdio.h>
//Char training. 

int main() {

  //This is a way of printing characters with ASCII, check ASCII table 
  char a = 65, b = 66, c = 67;
  //and a more easy way to print char
  char D = 'D';
  //If you try to print more than one character it will only print the last char
  char myText = 'Hello';
  printf("%c\n", myText);
  printf("%c\n", a);
  printf("%c\n", b);
  printf("%c\n", c);
  printf("%c\n",D);
  //there is a way to print more than one character we may create an array list 
  char myTextC[] = "Hello, c is a very cool programming language! :)";
  printf("%s", myTextC);
  return 0;

}