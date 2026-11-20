#include <stdio.h>

int main(void) {
    double saldo_medio, credito;
    scanf("%lf", &saldo_medio);

    if (saldo_medio > 1000.0) {
        credito = saldo_medio * 0.30;
    } else {
        credito = saldo_medio * 0.15;
    }

    printf("Saldo medio: R$ %.2f\n", saldo_medio);
    printf("Credito especial: R$ %.2f\n", credito);
    return 0;
}
