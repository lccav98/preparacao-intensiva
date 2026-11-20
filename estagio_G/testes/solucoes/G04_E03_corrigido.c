#include <stdio.h>

int soma_positivos(const int v[], int n);

int main(void) {
    int n, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    printf("Soma positivos: %d\n", soma_positivos(v, n));
    return 0;
}

int soma_positivos(const int v[], int n) {
    // Bug 1 original: caso base n == 1 retornava v[0] mesmo negativo e falhava para n == 0.
    if (n <= 0) {
        return 0;
    }
    // Bug 2 original: acessava v[n] fora dos limites em vez do ultimo elemento v[n - 1].
    if (v[n - 1] > 0) {
        return v[n - 1] + soma_positivos(v, n - 1);
    }
    return soma_positivos(v, n - 1);
}
