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

    int lin, col;
    scanf("%d %d", &lin, &col);
    int idx_l = lin - 1;
    int idx_c = col - 1;

    int soma_l = 0;
    printf("Linha %d:", lin);
    for (int j = 0; j < C; j++) {
        printf(" %d", m[idx_l][j]);
        soma_l += m[idx_l][j];
    }
    printf("\nSoma linha: %d\n", soma_l);

    int soma_c = 0;
    printf("Coluna %d:", col);
    for (int i = 0; i < L; i++) {
        printf(" %d", m[i][idx_c]);
        soma_c += m[i][idx_c];
    }
    printf("\nSoma coluna: %d\n", soma_c);

    return 0;
}
