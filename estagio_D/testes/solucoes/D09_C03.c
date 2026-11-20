#include <stdio.h>
#define MAX 225
#define INDICE(i, j, cols) ((i) * (cols) + (j))

int main(void) {
    int l, c, alvo;
    int v[MAX];

    scanf("%d %d", &l, &c);
    for (int i = 0; i < l; i++) {
        for (int j = 0; j < c; j++) {
            scanf("%d", &v[INDICE(i, j, c)]);
        }
    }
    scanf("%d", &alvo);

    for (int j = 0; j < c; j++) {
        int soma = 0;
        for (int i = 0; i < l; i++) {
            soma += v[INDICE(i, j, c)];
        }
        printf("Coluna %d: %d\n", j, soma);
    }

    int ocorrencias = 0, pos = -1;
    for (int idx = 0; idx < l * c; idx++) {
        if (v[idx] == alvo) {
            if (pos == -1) {
                pos = idx;
            }
            ocorrencias++;
        }
    }

    printf("Ocorrencias: %d\n", ocorrencias);
    if (pos == -1) {
        printf("Primeira: Nao encontrado\n");
    } else {
        printf("Primeira: (%d, %d)\n", pos / c, pos % c);
    }
    return 0;
}
