#include <stdio.h>

double media_vetor(const int v[], int n);

int main(void) {
    int n, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    printf("Media: %.2f\n", media_vetor(v, n));
    return 0;
}

double media_vetor(const int v[], int n) {
    if (n == 1) {
        return (double)v[0];
    }
    return ((n - 1) * media_vetor(v, n - 1) + v[n - 1]) / n;
}
