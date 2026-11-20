#include <stdio.h>

int main(void) {
    int inicio, fim;
    int impares = 0;
    int soma_mult3 = 0;
    int atual;

    scanf("%d %d", &inicio, &fim);

    atual = inicio;
    while (atual <= fim) {
        if (atual % 2 != 0) {
            impares++;
        }
        if (atual % 3 == 0) {
            soma_mult3 += atual;
        }
        atual++;
    }

    printf("Impares: %d\n", impares);
    printf("Soma mult 3: %d\n", soma_mult3);
    return 0;
}
