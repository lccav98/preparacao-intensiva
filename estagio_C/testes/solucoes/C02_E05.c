#include <stdio.h>

int main(void) {
    int a, b;
    int conta = 0;
    int soma = 0;
    int atual;

    scanf("%d %d", &a, &b);

    atual = a;
    while (atual <= b) {
        if (atual % 2 == 0) {
            conta++;
            soma += atual;
        }
        atual++;
    }

    printf("Quantidade: %d\n", conta);
    printf("Soma: %d\n", soma);
    return 0;
}
