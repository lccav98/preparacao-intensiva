#include <stdio.h>

double potencia_rapida(double x, int n, int *mult);

int main(void) {
    double x;
    int n, mult = 0;
    scanf("%lf %d", &x, &n);

    double res = potencia_rapida(x, n, &mult);
    printf("Potencia: %.2f\n", res);
    printf("Multiplicacoes: %d\n", mult);
    return 0;
}

double potencia_rapida(double x, int n, int *mult) {
    if (n < 0) {
        return 1.0 / potencia_rapida(x, -n, mult);
    }
    if (n == 0) {
        return 1.0;
    }
    if (n == 1) {
        return x;
    }
    double p = potencia_rapida(x, n / 2, mult);
    if (n % 2 == 0) {
        (*mult) += 1;
        return p * p;
    }
    (*mult) += 2;
    return x * p * p;
}
