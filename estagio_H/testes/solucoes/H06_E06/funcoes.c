#include "funcoes.h"

void ajustarBrilho(int img[ALTURA][LARGURA], int b) {
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            int novo = img[i][j] + b;
            if (novo < 0) {
                novo = 0;
            } else if (novo > 255) {
                novo = 255;
            }
            img[i][j] = novo;
        }
    }
}

void aplicarBlur(int img[ALTURA][LARGURA], int t) {
    static int aux[ALTURA][LARGURA];
    int r = t / 2;

    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            aux[i][j] = img[i][j];
        }
    }

    for (int i = r; i < ALTURA - r; i++) {
        for (int j = r; j < LARGURA - r; j++) {
            int soma = 0;
            for (int a = -r; a <= r; a++) {
                for (int b = -r; b <= r; b++) {
                    soma += img[i + a][j + b];
                }
            }
            aux[i][j] = soma / (t * t);
        }
    }

    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            img[i][j] = aux[i][j];
        }
    }
}

void ordenar(int v[], int n) {
    int i, j, temp;
    for (i = 0; i < n - 1; i++) {
        for (j = i + 1; j < n; j++) {
            if (v[i] > v[j]) {
                temp = v[i];
                v[i] = v[j];
                v[j] = temp;
            }
        }
    }
}

void aplicarMediana(int img[ALTURA][LARGURA]) {
    static int aux[ALTURA][LARGURA];
    int v[9];

    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            aux[i][j] = img[i][j];
        }
    }

    for (int i = 1; i < ALTURA - 1; i++) {
        for (int j = 1; j < LARGURA - 1; j++) {
            int k = 0;
            for (int a = -1; a <= 1; a++) {
                for (int b = -1; b <= 1; b++) {
                    v[k] = img[i + a][j + b];
                    k++;
                }
            }
            ordenar(v, 9);
            aux[i][j] = v[4];
        }
    }

    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            img[i][j] = aux[i][j];
        }
    }
}

void limiarizar(int img[ALTURA][LARGURA], int limiar) {
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            if (img[i][j] < limiar) {
                img[i][j] = 0;
            } else {
                img[i][j] = 255;
            }
        }
    }
}

void resumoImagem(const int img[ALTURA][LARGURA], int *min, int *max, double *media) {
    int mn = img[0][0];
    int mx = img[0][0];
    int soma = 0;

    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            if (img[i][j] < mn) {
                mn = img[i][j];
            }
            if (img[i][j] > mx) {
                mx = img[i][j];
            }
            soma += img[i][j];
        }
    }
    *min = mn;
    *max = mx;
    *media = (double)soma / (ALTURA * LARGURA);
}
