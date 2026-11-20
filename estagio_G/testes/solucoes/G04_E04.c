#include <stdio.h>

int contar_positivos(const int v[], int n);
int soma_pares(const int v[], int n);

int main(void) {
    int n, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    printf("Positivos: %d\n", contar_positivos(v, n));
    printf("Soma pares: %d\n", soma_pares(v, n));
    return 0;
}

int contar_positivos(const int v[], int n) {
    if (n <= 0) {
        return 0;
    }
    if (v[n - 1] > 0) {
        return 1 + contar_positivos(v, n - 1);
    }
    return contar_positivos(v, n - 1);
}

int soma_pares(const int v[], int n) {
    if (n <= 0) {
        return 0;
    }
    if (v[n - 1] % 2 == 0) {
        return v[n - 1] + soma_pares(v, n - 1);
    }
    return soma_pares(v, n - 1);
}
