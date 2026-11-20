#include <stdio.h>
#define L 3
#define C 5

int main(void) {
    int m[L][C];
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    int k;
    scanf("%d", &k);

    printf("Linhas:");
    for (int i = 0; i < L; i++) {
        int soma = 0;
        for (int j = 0; j < C; j++) {
            soma += m[i][j];
        }
        printf(" %d", soma);
    }
    printf("\n");

    printf("Coluna %d:", k);
    for (int i = 0; i < L; i++) {
        printf(" %d", m[i][k]);
    }
    printf("\n");

    return 0;
}
