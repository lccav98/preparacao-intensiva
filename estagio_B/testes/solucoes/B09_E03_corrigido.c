#include <stdio.h>

int main(void) {
    int prato, bebida;

    if (scanf("%d %d", &prato, &bebida) != 2) {
        return 1;
    }

    switch (prato) {
        case 1:
            printf("Prato: Peixe\n");
            switch (bebida) {
                case 1:
                    printf("Bebida: Suco\n");
                    break;
                case 2:
                    printf("Bebida: Agua\n");
                    break;
                default:
                    printf("Bebida Invalida\n");
                    break;
            }
            break;

        case 2:
            printf("Prato: Frango\n");
            switch (bebida) {
                case 1:
                    printf("Bebida: Suco\n");
                    break;
                case 2:
                    printf("Bebida: Agua\n");
                    break;
                default:
                    printf("Bebida Invalida\n");
                    break;
            }
            break;

        default:
            printf("Prato Invalido\n");
            break;
    }

    return 0;
}
