#include <stdio.h>
#define MAX 20

int main(void) {
    int N, A[MAX][MAX], P[MAX][MAX];
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            P[i][j] = 0;
            for (int k = 0; k < N; k++) {
                P[i][j] += A[i][k] * A[k][j];
            }
        }
    }

    int traco = 0;
    for (int i = 0; i < N; i++) {
        traco += P[i][i];
    }

    printf("A^2:\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", P[i][j]);
        }
        printf("\n");
    }
    printf("Traco de A^2: %d\n", traco);
    return 0;
}
