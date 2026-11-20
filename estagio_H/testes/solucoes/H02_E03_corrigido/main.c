#include <stdio.h>
#include "imagem.h"
// Correcao: incluir "funcoes.h" para declarar ajustarBrilho
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
    return 0;
}
