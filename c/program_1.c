#include <stdio.h>
#include <string.h>


typedef char *string;
string str = "Hello, World!";

void my_print(const char *s) {
  int i = 0;

  while (i < 300) {
    printf("%c", *(s + i));
    i++;
  }
}

void general_print() {
  printf("Size of str pointer: %lu\n", sizeof(str));
  printf("Size of dereferenced str pointer: %lu\n", sizeof(*str));
  printf("Strlen: %lu\n", strlen(str));
  printf("Printing everything: \n\n");
  my_print(str);
}

int main(int argc, char *argv[]) {
  string hello = "abcdef";

  printf("size: %lu\n", strlen(hello));

  {
    for(int i = 0; i < strlen(hello); i++) {
      printf("%c", *(hello + i));
    }
    printf("\n");
  }
  
  return 0;
}