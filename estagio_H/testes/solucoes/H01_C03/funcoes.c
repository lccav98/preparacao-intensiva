#include "funcoes.h"

void espelharHorizontal(int img[ALTURA][LARGURA]) {
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA / 2; j++) {
            int aux = img[i][j];
            img[i][j] = img[i][LARGURA - 1 - j];
            img[i][LARGURA - 1 - j] = aux;
        }
    }
}
