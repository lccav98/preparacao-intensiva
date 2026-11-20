#include "funcoes.h"

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

void copiarImagem(const int orig[ALTURA][LARGURA], int dest[ALTURA][LARGURA]) {
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            dest[i][j] = orig[i][j];
        }
    }
}

void aplicarMediana(int img[ALTURA][LARGURA]) {
    static int aux[ALTURA][LARGURA];
    int v[9];

    copiarImagem(img, aux);

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

    copiarImagem(aux, img);
}

int contarAlterados(const int a[ALTURA][LARGURA], const int b[ALTURA][LARGURA]) {
    int cont = 0;
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            if (a[i][j] != b[i][j]) {
                cont++;
            }
        }
    }
    return cont;
}
