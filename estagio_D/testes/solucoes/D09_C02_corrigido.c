#include <stdio.h>
#define LINHAS 3
#define COLUNAS 5
#define INDICE(i, j) ((i) * COLUNAS + (j))

int main(void) {
    char g[LINHAS * COLUNAS + 1];
    char buf[COLUNAS + 1];

    for (int i = 0; i < LINHAS; i++) {
        scanf("%5s", buf);
        for (int j = 0; j < COLUNAS; j++) {
            g[INDICE(i, j)] = buf[j];
        }
    }
    g[LINHAS * COLUNAS] = '\0';

    int lin1, col;
    scanf("%d %d", &lin1, &col);

    printf("Celula: %c\n", g[INDICE(lin1 - 1, col)]);
    printf("Coluna:");
    for (int i = 0; i < LINHAS; i++) {
        printf(" %c", g[INDICE(i, col)]);
    }
    printf("\nLinear: %s\n", g);
    return 0;
}
