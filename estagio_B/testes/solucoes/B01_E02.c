#include <stdio.h>

int main(void) {
    int valor, notas20, moedas1;
    scanf("%d", &valor);

    notas20 = valor / 20;
    moedas1 = valor % 20;

    printf("Notas de 20: %d\n", notas20);
    printf("Moedas de 1: %d\n", moedas1);
    return 0;
}
