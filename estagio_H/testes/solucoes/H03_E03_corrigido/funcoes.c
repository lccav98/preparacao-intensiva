#include "funcoes.h"

void aplicarBlur(int img[ALTURA][LARGURA], int t) {
    static int aux[ALTURA][LARGURA];
    int r = t / 2;

    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            aux[i][j] = img[i][j];
        }
    }

    // Correcao: usar i < ALTURA - r (nao <=) para preservar a borda inferior
    for (int i = r; i < ALTURA - r; i++) {
        for (int j = r; j < LARGURA - r; j++) {
            int soma = 0;
            for (int a = -r; a <= r; a++) {
                for (int b = -r; b <= r; b++) {
                    // Correcao: ler de aux (nao de img) para nao reutilizar pixels alterados
                    soma += aux[i + a][j + b];
                }
            }
            // Correcao: dividir por (t * t), total de pixels da janela t x t
            img[i][j] = soma / (t * t);
        }
    }
}
