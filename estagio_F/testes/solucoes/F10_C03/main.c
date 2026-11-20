#include <stdio.h>
#include "analise.h"

int main(void) {
    int linhas, m[10][COL], idx, mn, mx;
    char s[50], ch;

    scanf("%d", &linhas);
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < COL; j++) {
            scanf("%d", &m[i][j]);
        }
    }
    scanf("%d", &idx);
    scanf("%49s", s);
    scanf(" %c", &ch);

    linha_extremos(m, idx, &mn, &mx);
    printf("Linha %d: menor=%d maior=%d\n", idx, mn, mx);
    printf("Ocorrencias: %d\n", contar_ocorrencias_str(s, ch));
    return 0;
}
