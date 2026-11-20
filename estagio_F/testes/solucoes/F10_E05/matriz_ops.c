#include "matriz_ops.h"

int soma_diagonal_principal(const int m[][COL]) {
    int soma = 0;
    for (int i = 0; i < COL; i++) {
        soma += m[i][i];
    }
    return soma;
}

void extremos_matriz(const int m[][COL], int linhas, int *menor, int *maior) {
    *menor = m[0][0];
    *maior = m[0][0];
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < COL; j++) {
            if (m[i][j] < *menor) {
                *menor = m[i][j];
            }
            if (m[i][j] > *maior) {
                *maior = m[i][j];
            }
        }
    }
}
