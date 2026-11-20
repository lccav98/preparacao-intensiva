#include "funcoes.h"

void aplicarBlur(int img[ALTURA][LARGURA], int t) {
    static int aux[ALTURA][LARGURA];
    int r = t / 2;

    // Correcao: copiar img para aux antes de calcular para preservar as bordas
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            aux[i][j] = img[i][j];
        }
    }

    for (int i = r; i < ALTURA - r; i++) {
        for (int j = r; j < LARGURA - r; j++) {
            // Correcao: zerar soma dentro dos lacos i, j para cada pixel
            int soma = 0;
            // Correcao: percorrer janela completa de -r ate +r
            for (int a = -r; a <= r; a++) {
                for (int b = -r; b <= r; b++) {
                    soma += aux[i + a][j + b];
                }
            }
            img[i][j] = soma / (t * t);
        }
    }
}
