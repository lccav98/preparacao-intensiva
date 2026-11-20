#include <stdio.h>
#define MAX 20

int main(void) {
    int L, C, alvo;
    int A[MAX][MAX], B[MAX][MAX], T[MAX][MAX];

    scanf("%d %d", &L, &C);
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            scanf("%d", &A[i][j]);
        }
    }
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            scanf("%d", &B[i][j]);
        }
    }
    scanf("%d", &alvo);

    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            T[j][i] = A[i][j] + B[i][j];
        }
    }

    int li = -1, co = -1;
    for (int i = 0; i < C && li == -1; i++) {
        for (int j = 0; j < L; j++) {
            if (T[i][j] == alvo) {
                li = i;
                co = j;
                break;
            }
        }
    }

    printf("Transposta de A+B (%d x %d):\n", C, L);
    for (int i = 0; i < C; i++) {
        for (int j = 0; j < L; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", T[i][j]);
        }
        printf("\n");
    }
    if (li == -1) {
        printf("Busca em T: nao encontrado\n");
    } else {
        printf("Busca em T: (%d, %d)\n", li, co);
    }
    return 0;
}
