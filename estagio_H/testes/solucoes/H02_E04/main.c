#include <stdio.h>
#include "imagem.h"
#include "funcoes.h"

int main(void) {
    static int img[ALTURA][LARGURA];
    int b;

    if (!lerImagem(img)) {
        printf("Erro ao ler imagem.\n");
        return 0;
    }
    scanf("%d", &b);
    ajustarBrilho(img, b);
    salvarImagem(img);
    printf("Extremos (0 ou 255): %d\n", contarExtremos(img));
    return 0;
}
