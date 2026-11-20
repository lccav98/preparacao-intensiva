#include <stdio.h>
#include "imagem.h"
#include "funcoes.h"

int main(void) {
    static int img[ALTURA][LARGURA];
    int opcao, b, t;

    // Bug 1 corrigido: ler a imagem uma unica vez antes do menu para nao apagar filtros anteriores
    if (!lerImagem(img)) {
        printf("Erro ao ler imagem.\n");
        return 1;
    }

    do {
        printf("===== PROCESSAMENTO DE IMAGENS =====\n");
        printf("1 - Ajustar brilho\n");
        printf("2 - Aplicar desfoque (blur)\n");
        printf("3 - Aplicar filtro da mediana\n");
        printf("0 - Salvar e sair\n");
        printf("Escolha uma opcao:\n");
        if (scanf("%d", &opcao) != 1) {
            return 1;
        }

        switch (opcao) {
            case 1:
                scanf("%d", &b);
                ajustarBrilho(img, b);
                // Bug 2 corrigido: break obrigatorio para nao cair no case 2 (fall-through)
                break;
            case 2:
                scanf("%d", &t);
                // Bug 3 corrigido: validar t estritamente em {3, 5, 7}
                if (t == 3 || t == 5 || t == 7) {
                    aplicarBlur(img, t);
                } else {
                    printf("Tamanho invalido. Use 3, 5 ou 7.\n");
                }
                break;
            case 3:
                aplicarMediana(img);
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
