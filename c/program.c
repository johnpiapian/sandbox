#include <stdio.h>

void myprint(int *arr, size_t length) {
    for(size_t i=0; i<length; i++) {
        printf("%i \n", *(arr + i));
    }
}

int main(int argc, char *argv[]) {
    int arr[4] = {1, 2, 3, 4};

    myprint(arr, 4);

    return 0;
}