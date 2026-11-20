#include "analise.h"

void linha_extremos(const int m[][COL], int linha, int *menor, int *maior) {
    *menor = m[linha][0];
    *maior = m[linha][0];
    for (int j = 1; j < COL; j++) {
        if (m[linha][j] < *menor) {
            *menor = m[linha][j];
        }
        if (m[linha][j] > *maior) {
            *maior = m[linha][j];
        }
    }
}

int contar_ocorrencias_str(const char s[], char ch) {
    int cont = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == ch) {
            cont++;
        }
    }
    return cont;
}
