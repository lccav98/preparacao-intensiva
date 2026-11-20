#include <stdio.h>
#define MAX 100

int main(void) {
    int n, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    int pares[MAX], impares[MAX];
    int k_par = 0, k_imp = 0;
    for (int i = 0; i < n; i++) {
        if (v[i] % 2 == 0) {
            pares[k_par++] = v[i];
        } else {
            impares[k_imp++] = v[i];
        }
    }

    printf("Pares (%d):", k_par);
    if (k_par == 0) {
        printf(" nenhum");
    } else {
        for (int i = 0; i < k_par; i++) {
            printf(" %d", pares[i]);
        }
    }
    printf("\n");

    printf("Impares (%d):", k_imp);
    if (k_imp == 0) {
        printf(" nenhum");
    } else {
        for (int i = 0; i < k_imp; i++) {
            printf(" %d", impares[i]);
        }
    }
    printf("\n");

    return 0;
}
