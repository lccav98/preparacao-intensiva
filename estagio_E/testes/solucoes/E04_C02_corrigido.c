#include <stdio.h>
#define N 4

int main(void) {
    int m[N][N];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    int soma_sec = 0, soma_abaixo = 0;
    int eh_id = 1;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (i + j == N - 1) {
                soma_sec += m[i][j];
            }
            if (i > j) {
                soma_abaixo += m[i][j];
            }
            if ((i == j && m[i][j] != 1) || (i != j && m[i][j] != 0)) {
                eh_id = 0;
            }
        }
    }

    printf("Soma sec: %d\n", soma_sec);
    printf("Soma abaixo: %d\n", soma_abaixo);
    if (eh_id) {
        printf("Identidade: SIM\n");
    } else {
        printf("Identidade: NAO\n");
    }

    return 0;
}
