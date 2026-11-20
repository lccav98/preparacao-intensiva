#include <stdio.h>

int main(void) {
    double valor;
    scanf("%lf", &valor);

    if (valor >= 100.0) {
        valor = valor * 0.90;
    }

    printf("Valor final: R$ %.2f\n", valor);
    return 0;
}
