#include <stdio.h>

int main(void) {
    int n;
    int qtd = 0;
    int soma = 0;

    scanf("%d", &n);

    for (int i = 1; i <= n; i++) {
        if (i % 3 == 0 && i % 5 != 0) {
            printf("%d\n", i);
            qtd++;
            soma += i;
        }
    }

    printf("Quantidade: %d\n", qtd);
    printf("Soma: %d\n", soma);
    return 0;
}
