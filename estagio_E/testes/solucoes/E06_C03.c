#include <stdio.h>
#define MAX 20

int main(void) {
    int L, C, A[MAX][MAX], T[MAX][MAX], G[MAX][MAX];
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

    for (int i = 0; i < L; i++) {
        for (int j = 0; j < L; j++) {
            G[i][j] = 0;
            for (int k = 0; k < C; k++) {
                G[i][j] += A[i][k] * T[k][j];
            }
        }
    }

    printf("A * A^T (%d x %d):\n", L, L);
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < L; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", G[i][j]);
        }
        printf("\n");
    }
    return 0;
}
