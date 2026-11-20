#include <stdio.h>
#include "imagem.h"
#include "funcoes.h"

int main(void) {
    static int img[ALTURA][LARGURA];
    int passos;

    if (!lerImagem(img)) {
        printf("Erro ao ler imagem.\n");
        return 1;
    }
    scanf("%d", &passos);
    for (int p = 0; p < passos; p++) {
        aplicarMediana(img);
    }
    salvarImagem(img);
    return 0;
}
