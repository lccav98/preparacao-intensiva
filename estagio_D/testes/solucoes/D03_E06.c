#include <stdio.h>
#define MAX 100

int main(void) {
    int n, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    for (int i = 0; i < n / 2; i++) {
        int aux = v[i];
        v[i] = v[n - 1 - i];
        v[n - 1 - i] = aux;
    }

    int soma = 0;
    for (int i = 0; i < n; i++) {
        soma += v[i];
    }
    double media = (double)soma / n;

    int abaixo[MAX], acima_ig[MAX];
    int k_ab = 0, k_ac = 0;
    for (int i = 0; i < n; i++) {
        if (v[i] < media) {
            abaixo[k_ab++] = v[i];
        } else {
            acima_ig[k_ac++] = v[i];
        }
    }

    printf("Invertido:");
    for (int i = 0; i < n; i++) {
        printf(" %d", v[i]);
    }
    printf("\nMedia: %.2f\n", media);

    printf("Abaixo (%d):", k_ab);
    if (k_ab == 0) {
        printf(" nenhum");
    } else {
        for (int i = 0; i < k_ab; i++) {
            printf(" %d", abaixo[i]);
        }
    }
    printf("\n");

    printf("Acima ou igual (%d):", k_ac);
    if (k_ac == 0) {
        printf(" nenhum");
    } else {
        for (int i = 0; i < k_ac; i++) {
            printf(" %d", acima_ig[i]);
        }
    }
    printf("\n");

    return 0;
}
