#include <stdio.h>
#define L 3
#define C 3

int main(void) {
    int m[L][C];

    for (int i = 0; i < L; i++) {
        for (int j = 0; j < C; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    for (int i = L - 1; i >= 0; i--) {
        for (int j = 0; j < C; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", m[i][j]);
        }
        printf("\n");
    }

    return 0;
}
