#include <stdio.h>
#define MAX 20

int main(void) {
    int LA, CA, LB, CB;
    int A[MAX][MAX], B[MAX][MAX], C[MAX][MAX], D[MAX][MAX];

    scanf("%d %d", &LA, &CA);
    for (int i = 0; i < LA; i++) {
        for (int j = 0; j < CA; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    scanf("%d %d", &LB, &CB);
    for (int i = 0; i < LB; i++) {
        for (int j = 0; j < CB; j++) {
            scanf("%d", &B[i][j]);
        }
    }

    if (CA != LB) {
        printf("Produto A*B impossivel\n");
    } else {
        for (int i = 0; i < LA; i++) {
            for (int j = 0; j < CB; j++) {
                C[i][j] = 0;
                for (int k = 0; k < CA; k++) {
                    C[i][j] += A[i][k] * B[k][j];
                }
            }
        }
        printf("A*B (%d x %d):\n", LA, CB);
        for (int i = 0; i < LA; i++) {
            for (int j = 0; j < CB; j++) {
                if (j > 0) {
                    printf(" ");
                }
                printf("%d", C[i][j]);
            }
            printf("\n");
        }
    }

    if (CB != LA) {
        printf("Produto B*A impossivel\n");
    } else {
        for (int i = 0; i < LB; i++) {
            for (int j = 0; j < CA; j++) {
                D[i][j] = 0;
                for (int k = 0; k < CB; k++) {
                    D[i][j] += B[i][k] * A[k][j];
                }
            }
        }
        printf("B*A (%d x %d):\n", LB, CA);
        for (int i = 0; i < LB; i++) {
            for (int j = 0; j < CA; j++) {
                if (j > 0) {
                    printf(" ");
                }
                printf("%d", D[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}
