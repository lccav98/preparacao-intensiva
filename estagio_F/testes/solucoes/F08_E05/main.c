#include <stdio.h>
#include "matriz.h"

int main(void) {
    int linhas, c, m[10][COL];
    scanf("%d %d", &linhas, &c);
    ler_matriz(m, linhas);
    printf("Soma coluna %d: %d\n", c, soma_coluna(m, linhas, c));
    printf("Maior: %d\n", maior_matriz(m, linhas));
    return 0;
}
