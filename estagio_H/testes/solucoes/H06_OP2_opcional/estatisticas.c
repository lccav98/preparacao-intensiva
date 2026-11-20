#include "estatisticas.h"

int minimoImagem(const int img[ALTURA][LARGURA]) {
    int mn = img[0][0];
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            if (img[i][j] < mn) {
                mn = img[i][j];
            }
        }
    }
    return mn;
}

int maximoImagem(const int img[ALTURA][LARGURA]) {
    int mx = img[0][0];
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            if (img[i][j] > mx) {
                mx = img[i][j];
            }
        }
    }
    return mx;
}

double mediaImagem(const int img[ALTURA][LARGURA]) {
    int soma = 0;
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            soma += img[i][j];
        }
    }
    return (double)soma / (ALTURA * LARGURA);
}
