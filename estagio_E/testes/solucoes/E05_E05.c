#include <stdio.h>
#define MAX 20

int main(void) {
    int N, A[MAX][MAX], T[MAX][MAX], S[MAX][MAX];
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            T[j][i] = A[i][j];
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            S[i][j] = A[i][j] + T[i][j];
        }
    }

    int simA = 1;
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            if (A[i][j] != A[j][i]) {
                simA = 0;
                break;
            }
        }
        if (!simA) {
            break;
        }
    }

    int simS = 1;
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            if (S[i][j] != S[j][i]) {
                simS = 0;
                break;
            }
        }
        if (!simS) {
            break;
        }
    }

    printf("Simetrica A: %s\n", simA ? "Sim" : "Nao");
    printf("Matriz A + A^T:\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", S[i][j]);
        }
        printf("\n");
    }
    printf("Simetrica A + A^T: %s\n", simS ? "Sim" : "Nao");
    return 0;
}
