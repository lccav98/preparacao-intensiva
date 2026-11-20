#include <stdio.h>

int main(void) {
    double numerador, divisor;

    scanf("%lf", &numerador);

    do {
        scanf("%lf", &divisor);
        if (divisor == 0.0) {
            printf("Divisor invalido\n");
        }
    } while (divisor == 0.0);

    printf("Resultado: %.2f\n", numerador / divisor);
    return 0;
}
