#include <stdio.h>
#define MAX_L 10
#define MAX_C 10

int main(void) {
    int l, c;
    int m[MAX_L][MAX_C];
    scanf("%d %d", &l, &c);

    for (int i = 0; i < l; i++) {
        for (int j = 0; j < c; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    printf("Cantos: %d %d\n", m[0][0], m[l - 1][c - 1]);
    for (int i = 0; i < l; i++) {
        for (int j = 0; j < c; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", m[i][j]);
        }
        printf("\n");
    }

    return 0;
}
