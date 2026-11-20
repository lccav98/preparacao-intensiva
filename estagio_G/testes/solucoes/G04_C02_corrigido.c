#include <stdio.h>

int contar_acima(const int v[], int n, int lim);

int main(void) {
    int n, lim, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &lim);
    printf("Acima: %d\n", contar_acima(v, n, lim));
    return 0;
}

int contar_acima(const int v[], int n, int lim) {
    // Bug 1 original: acessava o vetor ANTES de testar if (n <= 0) (risco de v[-1]).
    if (n <= 0) {
        return 0;
    }
    // Bug 2 original: acessava v[n] em vez de v[n - 1].
    int ult = v[n - 1];
    if (ult > lim) {
        return 1 + contar_acima(v, n - 1, lim);
    }
    return contar_acima(v, n - 1, lim);
}
