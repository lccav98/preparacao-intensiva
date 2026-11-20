#include <stdio.h>

int main(void) {
    int quantia, n50, n20, n10, n1, resto;
    scanf("%d", &quantia);

    n50 = quantia / 50;
    resto = quantia % 50;

    n20 = resto / 20;
    resto = resto % 20;

    n10 = resto / 10;
    n1 = resto % 10;

    printf("Cedulas de 50: %d\n", n50);
    printf("Cedulas de 20: %d\n", n20);
    printf("Cedulas de 10: %d\n", n10);
    printf("Cedulas de 1: %d\n", n1);
    return 0;
}
