#include "funcoes.h"

void ajustarBrilhoLinhaRec(int img[ALTURA][LARGURA], int lin, int b) {
    if (lin == ALTURA) {
        return;
    }
    for (int j = 0; j < LARGURA; j++) {
        int novo = img[lin][j] + b;
        if (novo < 0) {
            novo = 0;
        } else if (novo > 255) {
            novo = 255;
        }
        img[lin][j] = novo;
    }
    ajustarBrilhoLinhaRec(img, lin + 1, b);
}
