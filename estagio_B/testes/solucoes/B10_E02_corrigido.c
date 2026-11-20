#include <stdio.h>

int main(void) {
    double lucro, imposto;

    if (scanf("%lf", &lucro) != 1) {
        return 1;
    }

    if (lucro < 10000.0) {
        imposto = 0.0;
    } else if (lucro <= 25000.0) {
        imposto = lucro * 0.10;
    } else {
        imposto = lucro * 0.15;
    }

    printf("Imposto: R$ %.2f\n", imposto);
    return 0;
}
