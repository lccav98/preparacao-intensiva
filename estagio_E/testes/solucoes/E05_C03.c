#include <stdio.h>
#define MAX 20

int main(void) {
    int N, A[MAX][MAX], B[MAX][MAX], S[MAX][MAX], T[MAX][MAX];
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &A[i][j]);
        }
    }
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &B[i][j]);
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            S[i][j] = A[i][j] + B[i][j];
            T[j][i] = S[i][j];
        }
    }

    int sim = 1;
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            if (S[i][j] != S[j][i]) {
                sim = 0;
                break;
            }
        }
        if (!sim) {
            break;
        }
    }

    printf("Transposta de (A + B):\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", T[i][j]);
        }
        printf("\n");
    }
    printf("Simetrica (A + B): %s\n", sim ? "Sim" : "Nao");
    return 0;
}
