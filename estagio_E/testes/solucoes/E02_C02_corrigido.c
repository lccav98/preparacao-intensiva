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

    int menor = m[0][0], li = 0, co = 0;
    for (int i = 0; i < l; i++) {
        for (int j = 0; j < c; j++) {
            if (m[i][j] < menor) {
                menor = m[i][j];
                li = i;
                co = j;
            }
        }
    }

    int pi = -1, pj = -1;
    for (int i = 0; i < l && pi == -1; i++) {
        for (int j = 0; j < c; j++) {
            if (m[i][j] == alvo) {
                pi = i;
                pj = j;
                break;
            }
        }
    }

    printf("Menor: %d (%d, %d)\n", menor, li, co);
    if (pi != -1) {
        printf("Posicao: (%d, %d)\n", pi, pj);
    } else {
        printf("Posicao: nao encontrada\n");
    }

    return 0;
}
