#include <stdio.h>

int produto_interno(const int a[], const int b[], int n);

int main(void) {
    int n, a[50], b[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }
    for (int i = 0; i < n; i++) {
        scanf("%d", &b[i]);
    }
    printf("Produto interno: %d\n", produto_interno(a, b, n));
    return 0;
}

int produto_interno(const int a[], const int b[], int n) {
    int soma = 0;
    for (int i = 0; i < n; i++) {
        soma += a[i] * b[i];
    }
    return soma;
}
