#include <stdio.h>

double media_vetor(const int v[], int n);
void analisar_vetor(const int v[], int n, int lim, int *acima_lim, double *media);

int main(void) {
    int n, v[50], lim, acima;
    double media;

    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &lim);

    analisar_vetor(v, n, lim, &acima, &media);
    printf("Media: %.2f\n", media);
    printf("Acima do limite: %d\n", acima);
    return 0;
}

double media_vetor(const int v[], int n) {
    int soma = 0;
    for (int i = 0; i < n; i++) {
        soma += v[i];
    }
    return (double)soma / n;
}

void analisar_vetor(const int v[], int n, int lim, int *acima_lim, double *media) {
    *media = media_vetor(v, n);
    int cont = 0;
    for (int i = 0; i < n; i++) {
        if (v[i] > lim) {
            cont++;
        }
    }
    *acima_lim = cont;
}
