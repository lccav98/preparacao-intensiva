#include <stdio.h>
#define LINHAS 3
#define COLUNAS 4
#define INDICE(i, j) ((i) * COLUNAS + (j))

int main(void) {
    int v[LINHAS * COLUNAS];

    for (int i = 0; i < LINHAS; i++) {
        for (int j = 0; j < COLUNAS; j++) {
            scanf("%d", &v[INDICE(i, j)]);
        }
    }

    int li, co;
    scanf("%d %d", &li, &co);

    for (int i = 0; i < LINHAS; i++) {
        for (int j = 0; j < COLUNAS; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", v[INDICE(i, j)]);
        }
        printf("\n");
    }

    printf("Consulta: %d\n", v[INDICE(li - 1, co - 1)]);
    return 0;
}
