#include <stdio.h>

int maior_vetor(const int v[], int n);
double media_vetor(const int v[], int n);
int contar_acima(const int v[], int n, double lim);

int main(void) {
    int n, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    double med = media_vetor(v, n);
    printf("Maior: %d\n", maior_vetor(v, n));
    printf("Media: %.2f\n", med);
    printf("Acima da media: %d\n", contar_acima(v, n, med));
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

int contar_acima(const int v[], int n, double lim) {
    if (n == 0) {
        return 0;
    }
    return (v[n - 1] > lim) + contar_acima(v, n - 1, lim);
}
