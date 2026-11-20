#include "funcoes.h"

// Correcao: implementacao movida de funcoes.h para funcoes.c
void zerarBordas(int img[ALTURA][LARGURA]) {
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            if (i == 0 || i == ALTURA - 1 || j == 0 || j == LARGURA - 1) {
                img[i][j] = 0;
            }
        }
    }
}
