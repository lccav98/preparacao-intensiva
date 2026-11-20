#include "funcoes.h"

void limiarizar(int img[ALTURA][LARGURA], int L) {
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            if (img[i][j] < L) {
                img[i][j] = 0;
            } else {
                // Correcao: usar else para incluir img[i][j] == L em 255
                img[i][j] = 255;
            }
        }
    }
}
