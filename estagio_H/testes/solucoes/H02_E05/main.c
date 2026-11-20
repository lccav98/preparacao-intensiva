#include <stdio.h>
#include "imagem.h"
#include "funcoes.h"

int main(void) {
    static int img[ALTURA][LARGURA];
    int b, limiar;

    if (!lerImagem(img)) {
        printf("Erro ao ler imagem.\n");
        return 0;
    }
    scanf("%d %d", &b, &limiar);
    ajustarBrilho(img, b);
    limiarizar(img, limiar);
    salvarImagem(img);
    return 0;
}
