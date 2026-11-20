#include <stdio.h>
#define MAX 20

int main(void) {
    int LA, CA, LB, CB;
    int A[MAX][MAX], B[MAX][MAX], C[MAX][MAX];

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
        printf("Multiplicacao impossivel\n");
    } else {
        for (int i = 0; i < LA; i++) {
            for (int j = 0; j < CB; j++) {
                C[i][j] = 0;
                for (int k = 0; k < CA; k++) {
                    C[i][j] += A[i][k] * B[k][j];
                }
            }
        }
        printf("Produto (%d x %d):\n", LA, CB);
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
    return 0;
}
