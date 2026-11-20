#include <stdio.h>
#define MAX 10

int main(void) {
    int l, c;
    int m[MAX][MAX];
    scanf("%d %d", &l, &c);

    for (int i = 0; i < l; i++) {
        for (int j = 0; j < c; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    printf("Linhas:");
    for (int i = 0; i < l; i++) {
        int soma = 0;
        for (int j = 0; j < c; j++) {
            soma += m[i][j];
        }
        printf(" %d", soma);
    }
    printf("\n");

    printf("Colunas:");
    for (int j = 0; j < c; j++) {
        int soma = 0;
        for (int i = 0; i < l; i++) {
            soma += m[i][j];
        }
        printf(" %d", soma);
    }
    printf("\n");

    return 0;
}
