#include <stdio.h>

int main(void) {
    int codigo, permissoes = 0;
    scanf("%d", &codigo);

    if (codigo % 2 == 0) {
        printf("Permissao de Leitura\n");
        permissoes = 1;
    }
    if (codigo % 3 == 0) {
        printf("Permissao de Escrita\n");
        permissoes = 1;
    }
    if (codigo % 5 == 0) {
        printf("Permissao de Execucao\n");
        permissoes = 1;
    }
    if (permissoes == 0) {
        printf("Sem permissoes especiais\n");
    }

    return 0;
}
