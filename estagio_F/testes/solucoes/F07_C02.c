#include <stdio.h>

#define N 3

int soma_diagonal_principal(const int m[][N]);
int soma_diagonal_secundaria(const int m[][N]);
void resumo_diagonais(const int m[][N], int *dp, int *ds);

int main(void) {
    int m[N][N], dp, ds;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &m[i][j]);
        }
    }
    resumo_diagonais(m, &dp, &ds);
    printf("Diagonal principal: %d\n", dp);
    printf("Diagonal secundaria: %d\n", ds);
    return 0;
}

int soma_diagonal_principal(const int m[][N]) {
    int soma = 0;
    for (int i = 0; i < N; i++) {
        soma += m[i][i];
    }
    return soma;
}

int soma_diagonal_secundaria(const int m[][N]) {
    int soma = 0;
    for (int i = 0; i < N; i++) {
        soma += m[i][N - 1 - i];
    }
    return soma;
}

void resumo_diagonais(const int m[][N], int *dp, int *ds) {
    *dp = soma_diagonal_principal(m);
    *ds = soma_diagonal_secundaria(m);
}
