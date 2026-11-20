#include <stdio.h>
#define MAX 10

int main(void) {
    int l, c;
    int m[MAX][MAX];
    scanf("%d %d", &l, &c);

    for (int i = 0; i < l; i++) {
        for (int j = 0; j < c; j++) {
            scanf("%d", &m[i][j]);
        }
    }

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
