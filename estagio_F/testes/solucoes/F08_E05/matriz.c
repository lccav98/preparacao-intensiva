#include <stdio.h>
#include "matriz.h"

void ler_matriz(int m[][COL], int linhas) {
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < COL; j++) {
            scanf("%d", &m[i][j]);
        }
    }
}

int soma_coluna(const int m[][COL], int linhas, int col) {
    int soma = 0;
    for (int i = 0; i < linhas; i++) {
        soma += m[i][col];
    }
    return soma;
}

int maior_matriz(const int m[][COL], int linhas) {
    int maior = m[0][0];
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < COL; j++) {
            if (m[i][j] > maior) {
                maior = m[i][j];
            }
        }
    }
    return maior;
}
