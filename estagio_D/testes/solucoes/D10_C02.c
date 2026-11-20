#include <stdio.h>
#define MAX 100

int main(void) {
    int m, n;
    int v[MAX], p[MAX], pos[MAX];

    scanf("%d", &m);
    for (int i = 0; i < m; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &n);
    for (int k = 0; k < n; k++) {
        scanf("%d", &p[k]);
    }

    int qtd = 0;
    for (int i = 0; i <= m - n; i++) {
        int casa = 1;
        for (int k = 0; k < n; k++) {
            if (v[i + k] != p[k]) {
                casa = 0;
                break;
            }
        }
        if (casa) {
            pos[qtd++] = i;
        }
    }

    printf("Ocorrencias: %d\nPosicoes:", qtd);
    if (qtd == 0) {
        printf(" Nenhuma\n");
    } else {
        for (int i = 0; i < qtd; i++) {
            printf(" %d", pos[i]);
        }
        printf("\n");
    }
    return 0;
}
