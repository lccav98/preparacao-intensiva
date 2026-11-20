#include <stdio.h>

int main(void) {
    int valor;
    int conta = 0;
    int soma = 0;
    int maior;

    scanf("%d", &valor);

    if (valor == 0) {
        printf("Nenhum valor valido\n");
    } else {
        maior = valor;
        while (valor != 0) {
            conta++;
            soma += valor;
            if (valor > maior) {
                maior = valor;
            }
            scanf("%d", &valor);
        }

        printf("Quantidade: %d\n", conta);
        printf("Soma: %d\n", soma);
        printf("Media: %.2f\n", (double)soma / conta);
        printf("Maior: %d\n", maior);
    }

    return 0;
}
