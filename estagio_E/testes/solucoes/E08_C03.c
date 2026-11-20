#include <stdio.h>
#define MAX 20

int main(void) {
    int N, A[MAX][MAX], B[MAX][MAX], P[MAX][MAX];
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
            P[i][j] = 0;
            for (int k = 0; k < N; k++) {
                P[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    int id = 1;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if ((i == j && P[i][j] != 1) || (i != j && P[i][j] != 0)) {
                id = 0;
                break;
            }
        }
        if (!id) {
            break;
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (P[i][j] < 0) {
                P[i][j] = 0;
            } else if (P[i][j] > 255) {
                P[i][j] = 255;
            }
        }
    }

    printf("Produto saturado [0, 255]:\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", P[i][j]);
        }
        printf("\n");
    }
    printf("Identidade (antes de saturar): %s\n", id ? "Sim" : "Nao");
    return 0;
}
