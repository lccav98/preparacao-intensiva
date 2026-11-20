#include <stdio.h>
#include "imagem.h"
#include "funcoes.h"

int main(void) {
    static int img[ALTURA][LARGURA];
    int t;

    if (!lerImagem(img)) {
        printf("Erro ao ler imagem.\n");
        return 0;
    }
    scanf("%d", &t);
    if (t != 3 && t != 5 && t != 7) {
        printf("Tamanho t invalido.\n");
        return 0;
    }
    aplicarBlur(img, t);
    salvarImagem(img);
    return 0;
}
