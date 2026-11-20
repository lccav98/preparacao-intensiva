#include <stdio.h>
#define MAX 20

int main(void) {
    int N, A[MAX][MAX];
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    printf("Somas linhas:");
    for (int i = 0; i < N; i++) {
        int s = 0;
        for (int j = 0; j < N; j++) {
            s += A[i][j];
        }
        printf(" %d", s);
    }
    printf("\n");

    printf("Somas colunas:");
    for (int j = 0; j < N; j++) {
        int s = 0;
        for (int i = 0; i < N; i++) {
            s += A[i][j];
        }
        printf(" %d", s);
    }
    printf("\n");

    int dp = 0, ds = 0, acima = 0, abaixo = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (i == j) {
                dp += A[i][j];
            } else if (j > i) {
                acima += A[i][j];
            } else {
                abaixo += A[i][j];
            }
            if (i + j == N - 1) {
                ds += A[i][j];
            }
        }
    }

    printf("Diagonal principal: %d\n", dp);
    printf("Diagonal secundaria: %d\n", ds);
    printf("Acima principal: %d\n", acima);
    printf("Abaixo principal: %d\n", abaixo);
    return 0;
}
