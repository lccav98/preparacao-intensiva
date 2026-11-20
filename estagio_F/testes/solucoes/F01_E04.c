#include <stdio.h>

void exibir_faixa(int ini, int fim) {
    if (ini > fim) {
        printf("Intervalo vazio\n");
    } else {
        for (int i = ini; i <= fim; i++) {
            if (i > ini) {
                printf(" ");
            }
            printf("%d", i);
        }
        printf("\n");
    }
}

int soma_intervalo(int ini, int fim) {
    int soma = 0;
    for (int i = ini; i <= fim; i++) {
        soma += i;
    }
    return soma;
}

int main(void) {
    int a, b;
    scanf("%d %d", &a, &b);
    exibir_faixa(a, b);
    printf("Soma: %d\n", soma_intervalo(a, b));
    return 0;
}
