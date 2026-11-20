#include <stdio.h>

int main(void) {
    double saldo = 100.0;
    double valor;
    int opcao;

    do {
        scanf("%d", &opcao);
        switch (opcao) {
            case 1:
                scanf("%lf", &valor);
                if (valor > 0.0) {
                    saldo += valor;
                    printf("Saldo: %.2f\n", saldo);
                } else {
                    printf("Valor invalido\n");
                }
                break;
            case 2:
                scanf("%lf", &valor);
                if (valor > 0.0 && valor <= saldo) {
                    saldo -= valor;
                    printf("Saldo: %.2f\n", saldo);
                } else {
                    printf("Operacao invalida\n");
                }
                break;
            case 3:
                printf("Saldo: %.2f\n", saldo);
                break;
            case 0:
                printf("Encerrando\n");
                break;
            default:
                printf("Opcao invalida\n");
                break;
        }
    } while (opcao != 0);

    return 0;
}
