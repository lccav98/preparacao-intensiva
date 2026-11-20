#include <stdio.h>
#define MAX 100

int main(void) {
    int n, m, v[MAX], p[MAX], pos[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &m);
    for (int k = 0; k < m; k++) {
        scanf("%d", &p[k]);
    }

    int qtd = 0;
    for (int i = 0; i <= n - m; i++) {
        int casou = 1;
        for (int k = 0; k < m; k++) {
            if (v[i + k] != p[k]) {
                casou = 0;
                break;
            }
        }
        if (casou) {
            pos[qtd++] = i;
        }
    }

    printf("Ocorrencias: %d\n", qtd);
    printf("Indices:");
    if (qtd == 0) {
        printf(" nenhum");
    } else {
        for (int i = 0; i < qtd; i++) {
            printf(" %d", pos[i]);
        }
    }
    printf("\n");
    return 0;
}
