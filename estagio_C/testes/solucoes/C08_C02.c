#include <stdio.h>

int main(void) {
    double x;
    int n;
    if (scanf("%lf %d", &x, &n) != 2) {
        return 1;
    }

    double soma = 0.0;
    double pot_x = x;
    double sinal = 1.0;

    for (int k = 1; k <= n; k++) {
        soma += sinal * pot_x / k;
        pot_x *= x;
        sinal = -sinal;
    }

    printf("ln(1+x) aprox: %.6f\n", soma);
    return 0;
}
