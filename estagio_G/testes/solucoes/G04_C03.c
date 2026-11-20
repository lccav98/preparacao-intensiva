#include <stdio.h>

int soma_intervalo_vetor(const int v[], int n, int min_val, int max_val);

int main(void) {
    int n, min_val, max_val, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d %d", &min_val, &max_val);
    printf("Soma no intervalo: %d\n", soma_intervalo_vetor(v, n, min_val, max_val));
    return 0;
}

int soma_intervalo_vetor(const int v[], int n, int min_val, int max_val) {
    if (n <= 0) {
        return 0;
    }
    if (v[n - 1] >= min_val && v[n - 1] <= max_val) {
        return v[n - 1] + soma_intervalo_vetor(v, n - 1, min_val, max_val);
    }
    return soma_intervalo_vetor(v, n - 1, min_val, max_val);
}
