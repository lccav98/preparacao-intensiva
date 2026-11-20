#include <stdio.h>
#include "matriz_ops.h"

int main(void) {
    int m[COL][COL], mn, mx;
    for (int i = 0; i < COL; i++) {
        for (int j = 0; j < COL; j++) {
            scanf("%d", &m[i][j]);
        }
    }
    extremos_matriz(m, COL, &mn, &mx);
    printf("Diagonal principal: %d\n", soma_diagonal_principal(m));
    printf("Menor: %d\n", mn);
    printf("Maior: %d\n", mx);
    return 0;
}
