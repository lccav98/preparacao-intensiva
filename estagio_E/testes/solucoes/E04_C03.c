#include <stdio.h>
#define MAX 10

int main(void) {
    int n;
    int m[MAX][MAX];
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    int soma_p = 0, soma_s = 0;
    for (int i = 0; i < n; i++) {
        soma_p += m[i][i];
        soma_s += m[i][n - 1 - i];
    }

    int soma_acima = 0, soma_abaixo = 0;
    int eh_id = 1;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (j > i) {
                soma_acima += m[i][j];
            } else if (i > j) {
                soma_abaixo += m[i][j];
            }
            if ((i == j && m[i][j] != 1) || (i != j && m[i][j] != 0)) {
                eh_id = 0;
            }
        }
    }

    printf("Soma principal: %d\n", soma_p);
    printf("Soma secundaria: %d\n", soma_s);
    printf("Soma acima: %d\n", soma_acima);
    printf("Soma abaixo: %d\n", soma_abaixo);
    if (eh_id) {
        printf("Identidade: SIM\n");
    } else {
        printf("Identidade: NAO\n");
    }

    return 0;
}
