#include <stdio.h>

int soma_pares(const int v[], int n);
int contem(const int v[], int n, int x);
double media_vetor(const int v[], int n);

int main(void) {
    int n, v[50], x;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &x);

    printf("Soma pares: %d\n", soma_pares(v, n));
    printf("Media: %.2f\n", media_vetor(v, n));
    if (contem(v, n, x)) {
        printf("Contem: Sim\n");
    } else {
        printf("Contem: Nao\n");
    }
    return 0;
}

int soma_pares(const int v[], int n) {
    if (n == 0) {
        return 0;
    }
    int termo = (v[n - 1] % 2 == 0) ? v[n - 1] : 0;
    return termo + soma_pares(v, n - 1);
}

int contem(const int v[], int n, int x) {
    if (n == 0) {
        return 0;
    }
    if (v[n - 1] == x) {
        return 1;
    }
    return contem(v, n - 1, x);
}

double media_vetor(const int v[], int n) {
    if (n == 1) {
        return (double)v[0];
    }
    return ((n - 1) * media_vetor(v, n - 1) + v[n - 1]) / n;
}
