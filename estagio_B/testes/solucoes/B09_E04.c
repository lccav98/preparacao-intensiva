#include <stdio.h>

int main(void) {
    double saldo = 1000.00;
    int op;
    double valor;

    if (scanf("%d", &op) != 1) {
        return 1;
    }

    switch (op) {
        case 1:
            if (scanf("%lf", &valor) != 1) {
                return 1;
            }
            if (valor <= 0.0) {
                printf("Valor Invalido\n");
            } else if (valor > saldo) {
                printf("Saldo Insuficiente\n");
            } else {
                saldo = saldo - valor;
                printf("Saldo Atual: R$ %.2f\n", saldo);
            }
            break;

        case 2:
            if (scanf("%lf", &valor) != 1) {
                return 1;
            }
            if (valor <= 0.0) {
                printf("Valor Invalido\n");
            } else {
                saldo = saldo + valor;
                printf("Saldo Atual: R$ %.2f\n", saldo);
            }
            break;

        case 3:
            printf("Saldo Atual: R$ %.2f\n", saldo);
            break;

        default:
            printf("Operacao Invalida\n");
            break;
    }

    return 0;
}
