#include <stdio.h>
#include "imagem.h"
#include "funcoes.h"

int main(void) {
    static int img[ALTURA][LARGURA];
    static int orig[ALTURA][LARGURA];

    if (!lerImagem(img)) {
        printf("Erro ao ler imagem.\n");
        return 1;
    }
    copiarImagem(img, orig);
    aplicarMediana(img);
    salvarImagem(img);
    printf("Pixels alterados: %d\n", contarAlterados(orig, img));
    return 0;
}
