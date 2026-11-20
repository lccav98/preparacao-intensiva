#include <stdio.h>

int main(void) {
    int categoria, item;

    if (scanf("%d %d", &categoria, &item) != 2) {
        return 1;
    }

    switch (categoria) {
        case 1:
            switch (item) {
                case 1:
                    printf("Suco Natural: R$ 7.00\n");
                    break;
                case 2:
                    printf("Refrigerante: R$ 5.00\n");
                    break;
                default:
                    printf("Item Invalido\n");
                    break;
            }
            break;

        case 2:
            switch (item) {
                case 1:
                    printf("Sanduiche: R$ 12.00\n");
                    break;
                case 2:
                    printf("Hamburguer: R$ 18.00\n");
                    break;
                default:
                    printf("Item Invalido\n");
                    break;
            }
            break;

        default:
            printf("Categoria Invalida\n");
            break;
    }

    return 0;
}
