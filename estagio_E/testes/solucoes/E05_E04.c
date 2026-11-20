#include <stdio.h>
#define MAX 20

int main(void) {
    int L, C, A[MAX][MAX], B[MAX][MAX], S[MAX][MAX], T[MAX][MAX];
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

    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            S[i][j] = A[i][j] + B[i][j];
            T[j][i] = S[i][j];
        }
    }

    printf("Soma (%d x %d):\n", L, C);
    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", S[i][j]);
        }
        printf("\n");
    }

    printf("Transposta da soma (%d x %d):\n", C, L);
    for (int i = 0; i < C; i++) {
        for (int j = 0; j < L; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", T[i][j]);
        }
        printf("\n");
    }
    return 0;
}
