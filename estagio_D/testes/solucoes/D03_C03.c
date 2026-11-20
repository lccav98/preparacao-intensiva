#include <stdio.h>
#define MAX 100

int main(void) {
    int n, limiar, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &limiar);

    int menores[MAX], maiores_ig[MAX];
    int k_men = 0, k_mai = 0;
    for (int i = 0; i < n; i++) {
        if (v[i] < limiar) {
            menores[k_men++] = v[i];
        } else {
            maiores_ig[k_mai++] = v[i];
        }
    }

    for (int i = 0; i < k_men / 2; i++) {
        int aux = menores[i];
        menores[i] = menores[k_men - 1 - i];
        menores[k_men - 1 - i] = aux;
    }

    printf("Menores invertidos (%d):", k_men);
    if (k_men == 0) {
        printf(" nenhum");
    } else {
        for (int i = 0; i < k_men; i++) {
            printf(" %d", menores[i]);
        }
    }
    printf("\n");

    printf("Maiores ou iguais (%d):", k_mai);
    if (k_mai == 0) {
        printf(" nenhum");
    } else {
        for (int i = 0; i < k_mai; i++) {
            printf(" %d", maiores_ig[i]);
        }
    }
    printf("\n");

    return 0;
}
