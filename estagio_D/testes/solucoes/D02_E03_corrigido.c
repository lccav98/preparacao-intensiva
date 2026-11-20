#include <stdio.h>
#define MAX 100

int main(void) {
    int n, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    int soma = 0, maior = v[0], menor = v[0];
    for (int i = 0; i < n; i++) {
        soma += v[i];
        if (v[i] > maior) {
            maior = v[i];
        }
        if (v[i] < menor) {
            menor = v[i];
        }
    }

    double media = (double)soma / n;
    printf("Media: %.2f\nMaior: %d\nMenor: %d\n", media, maior, menor);
    return 0;
}
