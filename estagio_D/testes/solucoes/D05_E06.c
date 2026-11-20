#include <stdio.h>
#define MAX 100

int main(void) {
    int n, m, v[MAX], p[MAX], r[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &m);
    for (int k = 0; k < m; k++) {
        scanf("%d", &p[k]);
    }

    int ocorrencias = 0;
    for (int i = 0; i <= n - m; i++) {
        int casou = 1;
        for (int k = 0; k < m; k++) {
            if (v[i + k] != p[k]) {
                casou = 0;
                break;
            }
        }
        if (casou) {
            ocorrencias++;
        }
    }

    printf("Ocorrencias: %d\n", ocorrencias);
    if (m > n) {
        printf("Convolucao: vazia\n");
    } else {
        int tam_r = n - m + 1;
        for (int i = 0; i <= n - m; i++) {
            int soma = 0;
            for (int k = 0; k < m; k++) {
                soma += v[i + k] * p[m - 1 - k];
            }
            r[i] = soma;
        }
        printf("Convolucao:");
        for (int i = 0; i < tam_r; i++) {
            printf(" %d", r[i]);
        }
        printf("\n");
    }

    return 0;
}
