#include <stdio.h>

int main(void) {
    int op;

    if (scanf("%d", &op) != 1) {
        return 1;
    }

    switch (op) {
        case 1:
            printf("Saldo\n");
            break;
        case 2:
            printf("Extrato\n");
            break;
        case 3:
            printf("Saque\n");
            break;
        default:
            printf("Opcao Invalida\n");
            break;
    }

    return 0;
}
