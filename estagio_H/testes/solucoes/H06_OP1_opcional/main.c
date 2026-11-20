#include <stdio.h>
#include "imagem.h"
#include "funcoes.h"

int main(void) {
    static int img[ALTURA][LARGURA];
    int b;

    if (!lerImagem(img)) {
        printf("Erro ao ler imagem.\n");
        return 1;
    }
    scanf("%d", &b);
    ajustarBrilhoLinhaRec(img, 0, b);
    salvarImagem(img);
    return 0;
}
