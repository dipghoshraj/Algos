#include <stdint.h>

void main(){
    printf("Hello World\n");

    char a[5]= {"a", "b", "c", "d", "e"}

    for (int i=0; i<5; i++){
        printf("%c", a[i]);
    }

    printf("\n");

    for (int i=4; i>=0; i--){
        printf("%c", a[i]);
    }
    printf("\n");
}