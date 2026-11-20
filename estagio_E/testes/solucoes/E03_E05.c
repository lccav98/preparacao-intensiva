#include <stdio.h>
#define N 4

int main(void) {
    int m[N][N];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    int maior_soma = 0;
    int idx_maior = 0;

    printf("Linhas:");
    for (int i = 0; i < N; i++) {
        int soma = 0;
        for (int j = 0; j < N; j++) {
            soma += m[i][j];
        }
        printf(" %d", soma);
        if (i == 0 || soma > maior_soma) {
            maior_soma = soma;
            idx_maior = i;
        }
    }
    printf("\n");

    printf("Colunas:");
    for (int j = 0; j < N; j++) {
        int soma = 0;
        for (int i = 0; i < N; i++) {
            soma += m[i][j];
        }
        printf(" %d", soma);
    }
    printf("\n");

    printf("Maior linha: %d (%d)\n", idx_maior, maior_soma);

    return 0;
}
