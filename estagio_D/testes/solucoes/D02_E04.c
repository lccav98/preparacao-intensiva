#include <stdio.h>
#define MAX 100

int main(void) {
    int n, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    int soma = 0;
    for (int i = 0; i < n; i++) {
        soma += v[i];
    }

    double media = (double)soma / n;
    int acima = 0;
    for (int i = 0; i < n; i++) {
        if (v[i] > media) {
            acima++;
        }
    }

    printf("Soma: %d\nMedia: %.2f\nAcima da media: %d\n", soma, media, acima);
    return 0;
}
