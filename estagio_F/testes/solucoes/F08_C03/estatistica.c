#include "estatistica.h"

double media_vetor(const int v[], int n) {
    int soma = 0;
    for (int i = 0; i < n; i++) {
        soma += v[i];
    }
    return (double)soma / n;
}

int contar_no_intervalo(const int v[], int n, int min, int max) {
    int cont = 0;
    for (int i = 0; i < n; i++) {
        if (v[i] >= min && v[i] <= max) {
            cont++;
        }
    }
    return cont;
}
