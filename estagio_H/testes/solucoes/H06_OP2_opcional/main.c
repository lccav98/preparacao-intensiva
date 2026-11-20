#include <stdio.h>
#include "imagem.h"
#include "funcoes.h"
#include "estatisticas.h"

int main(void) {
    static int img[ALTURA][LARGURA];
    int opcao, b, t;

    if (!lerImagem(img)) {
        printf("Erro ao ler imagem.\n");
        return 1;
    }

    do {
        printf("===== PROCESSAMENTO DE IMAGENS =====\n");
        printf("1 - Ajustar brilho\n");
        printf("2 - Aplicar desfoque (blur)\n");
        printf("3 - Aplicar filtro da mediana\n");
        printf("4 - Exibir estatisticas\n");
        printf("0 - Salvar e sair\n");
        printf("Escolha uma opcao:\n");
        if (scanf("%d", &opcao) != 1) {
            return 1;
        }

        switch (opcao) {
            case 1:
                scanf("%d", &b);
                ajustarBrilho(img, b);
                break;
            case 2:
                scanf("%d", &t);
                if (t == 3 || t == 5 || t == 7) {
                    aplicarBlur(img, t);
                } else {
                    printf("Tamanho invalido. Use 3, 5 ou 7.\n");
                }
                break;
            case 3:
                aplicarMediana(img);
                break;
            case 4:
                printf("Minimo: %d\n", minimoImagem(img));
                printf("Maximo: %d\n", maximoImagem(img));
                printf("Media: %.2f\n", mediaImagem(img));
                break;
            case 0:
                salvarImagem(img);
                break;
            default:
                printf("Opcao invalida.\n");
                break;
        }
    } while (opcao != 0);

    return 0;
}
