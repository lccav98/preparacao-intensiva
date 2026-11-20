#include <stdio.h>
#include <stdlib.h>
#define MAX 100

int main(void) {
    int n, alvo, v[MAX];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &alvo);

    int qtd = 0;
    printf("Ocorrencias:");
    for (int i = 0; i < n; i++) {
        if (v[i] == alvo) {
            printf(" %d", i);
            qtd++;
        }
    }
    if (qtd == 0) {
        printf(" nenhuma");
    }
    printf("\n");

    int melhor_dist = abs(v[0] - alvo);
    int pos_melhor = 0;
    for (int i = 1; i < n; i++) {
        int d = abs(v[i] - alvo);
        if (d < melhor_dist) {
            melhor_dist = d;
            pos_melhor = i;
        }
    }

    printf("Mais proximo: %d (indice %d)\n", v[pos_melhor], pos_melhor);
    return 0;
}
