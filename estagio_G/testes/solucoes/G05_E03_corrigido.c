#include <stdio.h>

int maior_vetor(const int v[], int n);
int contem(const int v[], int n, int x);

int main(void) {
    int n, x, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &x);
    printf("Maior: %d\n", maior_vetor(v, n));
    printf("Contem: %d\n", contem(v, n, x));
    return 0;
}

int maior_vetor(const int v[], int n) {
    // Bug 1 original: caso base n == 0 retornando 0 falhava quando todos eram negativos.
    if (n == 1) {
        return v[0];
    }
    // Bug 2 original: dupla chamada maior_vetor(v, n - 1) gerava custo O(2^n).
    int m = maior_vetor(v, n - 1);
    if (v[n - 1] > m) {
        return v[n - 1];
    }
    return m;
}

int contem(const int v[], int n, int x) {
    // Bug 3 original: testava v[n - 1] antes de verificar n <= 0 (acesso a v[-1]).
    if (n <= 0) {
        return 0;
    }
    if (v[n - 1] == x) {
        return 1;
    }
    return contem(v, n - 1, x);
}
