#include <stdio.h>
#define L 3
#define C 4

int main(void) {
    int m[L][C];
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    printf("Linhas:");
    for (int i = 0; i < L; i++) {
        int soma = 0;
        for (int j = 0; j < C; j++) {
            soma += m[i][j];
        }
        printf(" %d", soma);
    }
    printf("\n");

    printf("Colunas:");
    for (int j = 0; j < C; j++) {
        int soma_col = 0;
        for (int i = 0; i < L; i++) {
            soma_col += m[i][j];
        }
        printf(" %d", soma_col);
    }
    printf("\n");

    return 0;
}
