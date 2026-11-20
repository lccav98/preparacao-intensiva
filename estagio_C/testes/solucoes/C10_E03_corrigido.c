#include <stdio.h>

int main(void) {
    int n;
    if (scanf("%d", &n) != 1) {
        return 1;
    }

    if (n <= 0) {
        printf("Entrada Invalida\n");
        return 0;
    }

    double soma = 0.0;
    double sinal = 1.0;

    for (int k = 0; k < n; k++) {
        double den = (double)(n - k) * (n - k);
        soma += sinal / den;
        sinal = -sinal;
    }

    printf("S = %.6f\n", soma);
    return 0;
}
