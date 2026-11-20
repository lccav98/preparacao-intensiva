#include <stdio.h>
#define N 4

int main(void) {
    int m[N][N];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    printf("Diag principal:");
    for (int i = 0; i < N; i++) {
        printf(" %d", m[i][i]);
    }
    printf("\n");

    printf("Diag secundaria:");
    for (int i = 0; i < N; i++) {
        printf(" %d", m[i][N - 1 - i]);
    }
    printf("\n");

    int soma_acima = 0;
    int soma_abaixo = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (j > i) {
                soma_acima += m[i][j];
            } else if (i > j) {
                soma_abaixo += m[i][j];
            }
        }
    }

    printf("Soma acima: %d\n", soma_acima);
    printf("Soma abaixo: %d\n", soma_abaixo);

    return 0;
}
