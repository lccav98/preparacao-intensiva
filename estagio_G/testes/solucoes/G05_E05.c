#include <stdio.h>

int menor_vetor(const int v[], int n);
int contem(const int v[], int n, int x);

int main(void) {
    int n, x, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &x);
    printf("Menor: %d\n", menor_vetor(v, n));
    if (contem(v, n, x)) {
        printf("Encontrado: Sim\n");
    } else {
        printf("Encontrado: Nao\n");
    }
    return 0;
}

int menor_vetor(const int v[], int n) {
    if (n == 1) {
        return v[0];
    }
    int m = menor_vetor(v, n - 1);
    if (v[n - 1] < m) {
        return v[n - 1];
    }
    return m;
}

int contem(const int v[], int n, int x) {
    if (n <= 0) {
        return 0;
    }
    if (v[n - 1] == x) {
        return 1;
    }
    return contem(v, n - 1, x);
}
