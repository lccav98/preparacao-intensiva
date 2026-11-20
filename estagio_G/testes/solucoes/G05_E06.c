#include <stdio.h>

int maior_vetor(const int v[], int n);
double media_vetor(const int v[], int n);

int main(void) {
    int n, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    printf("Maior: %d\n", maior_vetor(v, n));
    printf("Media: %.2f\n", media_vetor(v, n));
    return 0;
}

int maior_vetor(const int v[], int n) {
    if (n == 1) {
        return v[0];
    }
    int m = maior_vetor(v, n - 1);
    if (v[n - 1] > m) {
        return v[n - 1];
    }
    return m;
}

double media_vetor(const int v[], int n) {
    if (n == 1) {
        return (double)v[0];
    }
    return ((n - 1) * media_vetor(v, n - 1) + v[n - 1]) / n;
}
