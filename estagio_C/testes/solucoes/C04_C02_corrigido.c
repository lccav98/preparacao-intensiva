#include <stdio.h>

int main(void) {
    int op;
    int cont = 0;

    do {
        scanf("%d", &op);
        switch (op) {
            case 1:
                cont++;
                printf("Item adicionado\n");
                break;
            case 0:
                printf("Total: %d\n", cont);
                break;
            default:
                printf("Opcao invalida\n");
                break;
        }
    } while (op != 0);

    return 0;
}
