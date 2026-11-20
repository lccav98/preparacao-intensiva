#include <stdio.h>
#define MAX 400
#define INDICE(i, j, cols) ((i) * (cols) + (j))

int main(void) {
    int l, c;
    int v[MAX];

    scanf("%d %d", &l, &c);
    for (int i = 0; i < l; i++) {
        for (int j = 0; j < c; j++) {
            scanf("%d", &v[INDICE(i, j, c)]);
        }
    }

    for (int i = 0; i < l; i++) {
        int soma = 0;
        for (int j = 0; j < c; j++) {
            soma += v[INDICE(i, j, c)];
        }
        printf("Linha %d: %d\n", i, soma);
    }

    int maior = v[0], idx_maior = 0;
    for (int idx = 1; idx < l * c; idx++) {
        if (v[idx] > maior) {
            maior = v[idx];
            idx_maior = idx;
        }
    }

    printf("Maior: %d em (%d, %d)\n", maior, idx_maior / c, idx_maior % c);
    return 0;
}
