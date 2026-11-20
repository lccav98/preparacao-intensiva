#include <stdio.h>
#define L 3
#define C 4

int main(void) {
    int m[L][C];
    int soma = 0;

    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            scanf("%d", &m[i][j]);
            soma += m[i][j];
        }
    }

    double media = (double)soma / (L * C);
    int acima = 0;
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            if (m[i][j] > media) {
                acima++;
            }
        }
    }

    printf("Media: %.2f\n", media);
    printf("Acima da media: %d\n", acima);

    return 0;
}
