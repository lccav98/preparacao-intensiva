#include "funcoes.h"

void inverterCores(int img[ALTURA][LARGURA]) {
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            img[i][j] = 255 - img[i][j];
        }
    }
}
