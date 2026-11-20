#include <stdio.h>

int main(void) {
    int x;
    scanf("%d", &x);

    if (x > 0) {
        printf("Positivo\n");
    }

    if (x == 10) {
        printf("Numero igual a 10\n");
    }

    printf("Fim\n");
    return 0;
}
