#include <stdio.h>

void substituir_negativos(int v[], int n);
void imprimir_vetor(const int v[], int n);

int main(void) {
    int n, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    substituir_negativos(v, n);
    imprimir_vetor(v, n);
    return 0;
}

void substituir_negativos(int v[], int n) {
    for (int i = 0; i < n; i++) {
        if (v[i] < 0) {
            v[i] = 0;
        }
    }
}

void imprimir_vetor(const int v[], int n) {
    for (int i = 0; i < n; i++) {
        if (i > 0) {
            printf(" ");
        }
        printf("%d", v[i]);
    }
    printf("\n");
}
