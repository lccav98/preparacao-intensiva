#include <stdio.h>

double media_vetor(const int v[], int n);
int contar_acima(const int v[], int n, double lim);

int main(void) {
    int n, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    double m = media_vetor(v, n);
    printf("Media: %.2f\n", m);
    printf("Acima da media: %d\n", contar_acima(v, n, m));
    return 0;
}

double media_vetor(const int v[], int n) {
    if (n == 1) {
        return (double)v[0];
    }
    return ((n - 1) * media_vetor(v, n - 1) + v[n - 1]) / n;
}

int contar_acima(const int v[], int n, double lim) {
    if (n <= 0) {
        return 0;
    }
    if (v[n - 1] > lim) {
        return 1 + contar_acima(v, n - 1, lim);
    }
    return contar_acima(v, n - 1, lim);
}
