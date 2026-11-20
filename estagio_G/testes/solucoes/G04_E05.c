#include <stdio.h>

int contar_ocorrencias(const int v[], int n, int x);

int main(void) {
    int n, x, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &x);
    printf("Ocorrencias: %d\n", contar_ocorrencias(v, n, x));
    return 0;
}

int contar_ocorrencias(const int v[], int n, int x) {
    if (n <= 0) {
        return 0;
    }
    if (v[n - 1] == x) {
        return 1 + contar_ocorrencias(v, n - 1, x);
    }
    return contar_ocorrencias(v, n - 1, x);
}
