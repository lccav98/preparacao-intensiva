#include <stdio.h>

int main(void) {
    int x;
    int conta = 0;
    int soma = 0;

    scanf("%d", &x);

    while (x != 0) {
        soma += x;
        conta++;
        scanf("%d", &x);
    }

    printf("Quantidade: %d\n", conta);
    printf("Soma: %d\n", soma);
    return 0;
}
