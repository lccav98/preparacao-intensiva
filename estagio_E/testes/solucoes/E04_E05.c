#include <stdio.h>
#define MAX 10

int main(void) {
    int n;
    int m[MAX][MAX];
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &m[i][j]);
        }
    }

    printf("Diag principal:");
    for (int i = 0; i < n; i++) {
        printf(" %d", m[i][i]);
    }
    printf("\n");

    printf("Diag secundaria:");
    for (int i = 0; i < n; i++) {
        printf(" %d", m[i][n - 1 - i]);
    }
    printf("\n");

    int eh_id = 1;
    for (int i = 0; i < n && eh_id; i++) {
        for (int j = 0; j < n; j++) {
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
