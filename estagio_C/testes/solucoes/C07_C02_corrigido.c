#include <stdio.h>

int main(void) {
    int opcao;
    int rodando = 1;

    while (rodando) {
        if (scanf("%d", &opcao) != 1) {
            break;
        }
        switch (opcao) {
            case 1:
                printf("Opcao 1 Executada\n");
                break;
            case 0:
                printf("Saindo\n");
                rodando = 0;
                break;
            default:
                printf("Opcao Invalida\n");
                break;
        }
    }

    printf("Fim do Programa\n");
    return 0;
}
