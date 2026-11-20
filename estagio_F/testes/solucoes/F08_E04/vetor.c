#include <stdio.h>
#include "vetor.h"

void ler_vetor(int v[], int n) {
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
}

int soma_vetor(const int v[], int n) {
    int soma = 0;
    for (int i = 0; i < n; i++) {
        soma += v[i];
    }
    return soma;
}

int maior_vetor(const int v[], int n) {
    int maior = v[0];
    for (int i = 1; i < n; i++) {
        if (v[i] > maior) {
            maior = v[i];
        }
    }
    return maior;
}
