#include <stdio.h>
#define L 4
#define C 5

int main(void) {
    int m[L][C];
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    int soma = 0;
    int maior = m[0][0], li_max = 0, co_max = 0;
    int menor = m[0][0], li_min = 0, co_min = 0;

    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            soma += m[i][j];
            if (m[i][j] > maior) {
                maior = m[i][j];
                li_max = i;
                co_max = j;
            }
            if (m[i][j] < menor) {
                menor = m[i][j];
                li_min = i;
                co_min = j;
            }
        }
    }

    printf("Soma: %d\n", soma);
    printf("Maior: %d (%d, %d)\n", maior, li_max, co_max);
    printf("Menor: %d (%d, %d)\n", menor, li_min, co_min);

    return 0;
}
