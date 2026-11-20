#include <stdio.h>
#define MAX 20

int main(void) {
    int L1, C1, L2, C2;
    int A[MAX][MAX], B[MAX][MAX], S[MAX][MAX];

    scanf("%d %d", &L1, &C1);
    for (int i = 0; i < L1; i++) {
        for (int j = 0; j < C1; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    scanf("%d %d", &L2, &C2);
    for (int i = 0; i < L2; i++) {
        for (int j = 0; j < C2; j++) {
            scanf("%d", &B[i][j]);
        }
    }

    if (L1 != L2 || C1 != C2) {
        printf("Soma impossivel\n");
    } else {
        for (int i = 0; i < L1; i++) {
            for (int j = 0; j < C1; j++) {
                S[i][j] = A[i][j] + B[i][j];
            }
        }
        printf("Soma:\n");
        for (int i = 0; i < L1; i++) {
            for (int j = 0; j < C1; j++) {
                if (j > 0) {
                    printf(" ");
                }
                printf("%d", S[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}
