#include <stdio.h>
#define L 3
#define C 3

int main(void) {
    int m[L][C];
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    int alvo;
    scanf("%d", &alvo);

    int soma = 0;
    int maior = m[0][0], li = 0, co = 0;
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            soma += m[i][j];
            if (m[i][j] > maior) {
                maior = m[i][j];
                li = i;
                co = j;
            }
        }
    }

    int ai = -1, aj = -1;
    for (int i = 0; i < L && ai == -1; i++) {
        for (int j = 0; j < C; j++) {
            if (m[i][j] == alvo) {
                ai = i;
                aj = j;
                break;
            }
        }
    }

    printf("Soma: %d\n", soma);
    printf("Maior: %d (%d, %d)\n", maior, li, co);
    if (ai != -1) {
        printf("Alvo: (%d, %d)\n", ai, aj);
    } else {
        printf("Alvo: nao encontrado\n");
    }

    return 0;
}
