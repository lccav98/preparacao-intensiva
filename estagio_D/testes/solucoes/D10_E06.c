#include <stdio.h>
#define MAX 225
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

    printf("Transposta:\n");
    for (int j = 0; j < c; j++) {
        for (int i = 0; i < l; i++) {
            if (i > 0) {
                printf(" ");
            }
            printf("%d", v[INDICE(i, j, c)]);
        }
        printf("\n");
    }

    int maior = v[0], idx_maior = 0;
    int menor = v[0], idx_menor = 0;
    for (int idx = 1; idx < l * c; idx++) {
        if (v[idx] > maior) {
            maior = v[idx];
            idx_maior = idx;
        }
        if (v[idx] <= menor) {
            menor = v[idx];
            idx_menor = idx;
        }
    }

    printf("Maior: %d em (%d, %d)\n", maior, idx_maior / c, idx_maior % c);
    printf("Menor: %d em (%d, %d)\n", menor, idx_menor / c, idx_menor % c);
    return 0;
}
