#include <stdio.h>

int maior_de_dois(int a, int b) {
    // Erro 1 original: faltava o tipo 'int' antes de 'b' na lista de parametros.
    // Erro 2 original: faltava o comando 'return b;' quando a < b.
    if (a >= b) {
        return a;
    }
    return b;
}

int main(void) {
    int x, y, m;
    scanf("%d %d", &x, &y);
    // Erro 3 original: chamada maior_de_dois(x, y); descartava o valor retornado.
    m = maior_de_dois(x, y);
    printf("Maior: %d\n", m);
    return 0;
}
