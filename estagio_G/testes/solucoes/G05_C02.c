#include <stdio.h>

int indice_ultimo(const int v[], int n, int x);

int main(void) {
    int n, x, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &x);
    printf("Indice: %d\n", indice_ultimo(v, n, x));
    return 0;
}

int indice_ultimo(const int v[], int n, int x) {
    if (n <= 0) {
        return -1;
    }
    if (v[n - 1] == x) {
        return n - 1;
    }
    return indice_ultimo(v, n - 1, x);
}
