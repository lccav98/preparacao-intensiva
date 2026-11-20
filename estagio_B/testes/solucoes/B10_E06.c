#include <stdio.h>

int main(void) {
    int tipo;
    double kwh;

    if (scanf("%d %lf", &tipo, &kwh) != 2) {
        return 1;
    }

    if (kwh < 0.0) {
        printf("Consumo Invalido\n");
    } else {
        double valor;
        switch (tipo) {
            case 1:
                if (kwh <= 100.0) {
                    valor = kwh * 0.60;
                } else {
                    valor = 60.00 + (kwh - 100.0) * 0.85;
                }
                printf("Fatura Residencial: R$ %.2f\n", valor);
                break;

            case 2:
                if (kwh <= 200.0) {
                    valor = kwh * 0.75;
                } else {
                    valor = 150.00 + (kwh - 200.0) * 0.95;
                }
                printf("Fatura Comercial: R$ %.2f\n", valor);
                break;

            case 3:
                valor = 300.00 + kwh * 0.50;
                printf("Fatura Industrial: R$ %.2f\n", valor);
                break;

            default:
                printf("Tipo Invalido\n");
                break;
        }
    }

    return 0;
}
