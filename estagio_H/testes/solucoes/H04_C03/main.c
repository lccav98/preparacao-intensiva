#include <stdio.h>
#include "imagem.h"
#include "funcoes.h"

int main(void) {
    static int img[ALTURA][LARGURA];
    int limiar;

    if (!lerImagem(img)) {
        printf("Erro ao ler imagem.\n");
        return 1;
    }
    scanf("%d", &limiar);
    aplicarMediana(img);
    limiarizar(img, limiar);
    salvarImagem(img);
    return 0;
}
