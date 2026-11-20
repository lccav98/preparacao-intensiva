#include <stdio.h>
#define MAX 100

int main(void) {
    int n, m;
    int v[MAX], h[MAX], r[MAX];

    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &m);
    for (int k = 0; k < m; k++) {
        scanf("%d", &h[k]);
    }

    int tam_r = n - m + 1;
    for (int i = 0; i < tam_r; i++) {
        int soma = 0;
        for (int k = 0; k < m; k++) {
            soma += v[i + k] * h[m - 1 - k];
        }
        r[i] = soma;
    }

    printf("Convolucao:");
    for (int i = 0; i < tam_r; i++) {
        printf(" %d", r[i]);
    }
    printf("\n");
    return 0;
}
