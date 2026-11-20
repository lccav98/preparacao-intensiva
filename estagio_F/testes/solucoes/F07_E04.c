#include <stdio.h>

#define N 3

int eh_simetrica(const int m[][N]);

int main(void) {
    int m[N][N];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &m[i][j]);
        }
    }
    if (eh_simetrica(m)) {
        printf("Simetrica: Sim\n");
    } else {
        printf("Simetrica: Nao\n");
    }
    return 0;
}

int eh_simetrica(const int m[][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            if (m[i][j] != m[j][i]) {
                return 0;
            }
        }
    }
    return 1;
}
