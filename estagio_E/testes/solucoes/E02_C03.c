#include <stdio.h>
#define MAX 10

int main(void) {
    int l, c;
    int m[MAX][MAX];
    scanf("%d %d", &l, &c);

    for (int i = 0; i < l; i++) {
        for (int j = 0; j < c; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    int alvo;
    scanf("%d", &alvo);

    int soma = 0;
    int maior = m[0][0], li = 0, co = 0;
    for (int i = 0; i < l; i++) {
        for (int j = 0; j < c; j++) {
            soma += m[i][j];
            if (m[i][j] > maior) {
                maior = m[i][j];
                li = i;
                co = j;
            }
        }
    }

    int bi = -1, bj = -1;
    for (int i = 0; i < l && bi == -1; i++) {
        for (int j = 0; j < c; j++) {
            if (m[i][j] == alvo) {
                bi = i;
                bj = j;
                break;
            }
        }
    }

    printf("Soma: %d\n", soma);
    printf("Maior: %d (%d, %d)\n", maior, li, co);
    if (bi != -1) {
        printf("Busca: (%d, %d)\n", bi, bj);
    } else {
        printf("Busca: nao encontrado\n");
    }

    return 0;
}
