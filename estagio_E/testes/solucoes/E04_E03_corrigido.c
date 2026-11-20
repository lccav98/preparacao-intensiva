#include <stdio.h>
#define N 3

int main(void) {
    int m[N][N];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    printf("Diag secundaria:");
    for (int i = 0; i < N; i++) {
        printf(" %d", m[i][N - 1 - i]);
    }
    printf("\n");

    int eh_id = 1;
    for (int i = 0; i < N && eh_id; i++) {
        for (int j = 0; j < N; j++) {
            if ((i == j && m[i][j] != 1) || (i != j && m[i][j] != 0)) {
                eh_id = 0;
                break;
            }
        }
    }

    if (eh_id) {
        printf("Identidade: SIM\n");
    } else {
        printf("Identidade: NAO\n");
    }

    return 0;
}
