#include <stdio.h>

int soma_pares(const int v[], int n);

int main(void) {
    int n, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    printf("Soma pares: %d\n", soma_pares(v, n));
    return 0;
}

int soma_pares(const int v[], int n) {
    int soma = 0;
    for (int i = 0; i < n; i++) {
        if (v[i] % 2 == 0) {
            soma += v[i];
        }
    }
    return soma;
}
