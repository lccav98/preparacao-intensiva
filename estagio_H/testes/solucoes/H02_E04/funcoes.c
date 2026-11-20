#include "funcoes.h"

void ajustarBrilho(int img[ALTURA][LARGURA], int b) {
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            img[i][j] += b;
            if (img[i][j] < 0) {
                img[i][j] = 0;
            } else if (img[i][j] > 255) {
                img[i][j] = 255;
            }
        }
    }
}

int contarExtremos(const int img[ALTURA][LARGURA]) {
    int cont = 0;
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            if (img[i][j] == 0 || img[i][j] == 255) {
                cont++;
            }
        }
    }
    return cont;
}
