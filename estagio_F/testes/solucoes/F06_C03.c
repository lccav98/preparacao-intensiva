#include <stdio.h>

void estatisticas_vetor(const int v[], int n, int *menor, int *maior, double *media);

int main(void) {
    int n, v[50], menor, maior;
    double media;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    estatisticas_vetor(v, n, &menor, &maior, &media);
    printf("Menor: %d\nMaior: %d\nMedia: %.2f\n", menor, maior, media);
    return 0;
}

void estatisticas_vetor(const int v[], int n, int *menor, int *maior, double *media) {
    int soma = v[0];
    *menor = v[0];
    *maior = v[0];
    for (int i = 1; i < n; i++) {
        soma += v[i];
        if (v[i] < *menor) {
            *menor = v[i];
        }
        if (v[i] > *maior) {
            *maior = v[i];
        }
    }
    *media = (double)soma / n;
}
