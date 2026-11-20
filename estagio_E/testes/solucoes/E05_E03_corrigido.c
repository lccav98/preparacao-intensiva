#include <stdio.h>
#define MAX 20

int main(void) {
    int L, C, A[MAX][MAX], T[MAX][MAX];
    scanf("%d %d", &L, &C);
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            T[j][i] = A[i][j];
        }
    }

    int sim = 1;
    if (L != C) {
        sim = 0;
    } else {
        for (int i = 0; i < L; i++) {
            for (int j = i + 1; j < C; j++) {
                if (A[i][j] != A[j][i]) {
                    sim = 0;
                    break;
                }
            }
            if (!sim) {
                break;
            }
        }
    }

    printf("Transposta (%d x %d):\n", C, L);
    for (int i = 0; i < C; i++) {
        for (int j = 0; j < L; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", T[i][j]);
        }
        printf("\n");
    }
    printf("Simetrica: %s\n", sim ? "Sim" : "Nao");
    return 0;
}
