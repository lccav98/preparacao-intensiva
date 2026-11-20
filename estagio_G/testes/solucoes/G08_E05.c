#include <stdio.h>

double pot_linear(double x, int n, int *chamadas);
double pot_rapida(double x, int n, int *chamadas);

int main(void) {
    double x;
    int n, c_lin = 0, c_rap = 0;
    scanf("%lf %d", &x, &n);

    pot_linear(x, n, &c_lin);
    double r = pot_rapida(x, n, &c_rap);

    printf("Resultado: %.2f\n", r);
    printf("Chamadas linear: %d\n", c_lin);
    printf("Chamadas rapida: %d\n", c_rap);
    return 0;
}

double pot_linear(double x, int n, int *chamadas) {
    (*chamadas)++;
    if (n == 0) {
        return 1.0;
    }
    if (n == 1) {
        return x;
    }
    return x * pot_linear(x, n - 1, chamadas);
}

double pot_rapida(double x, int n, int *chamadas) {
    (*chamadas)++;
    if (n == 0) {
        return 1.0;
    }
    if (n == 1) {
        return x;
    }
    double p = pot_rapida(x, n / 2, chamadas);
    if (n % 2 == 0) {
        return p * p;
    }
    return x * p * p;
}
