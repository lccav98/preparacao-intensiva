#include <stdio.h>
#include "imagem.h"

int lerImagem(int img[ALTURA][LARGURA]) {
    char tipo[4];
    int larg, alt, maxval;
    if (scanf("%3s %d %d %d", tipo, &larg, &alt, &maxval) != 4) {
        return 0;
    }
    if (tipo[0] != 'P' || tipo[1] != '2' || tipo[2] != '\0') {
        return 0;
    }
    if (larg != LARGURA || alt != ALTURA || maxval != 255) {
        return 0;
    }
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            if (scanf("%d", &img[i][j]) != 1) {
                return 0;
            }
        }
    }
    return 1;
}

void salvarImagem(const int img[ALTURA][LARGURA]) {
    printf("P2\n%d %d\n255\n", LARGURA, ALTURA);
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", img[i][j]);
        }
        printf("\n");
    }
}
