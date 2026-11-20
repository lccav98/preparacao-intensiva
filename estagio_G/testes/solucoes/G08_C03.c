#include <stdio.h>

int fib(int n);
double potencia_rapida(double x, int n, int *chamadas);

int main(void) {
    double x;
    int n, k, chamadas = 0;
    scanf("%lf %d %d", &x, &n, &k);

    double pot = potencia_rapida(x, n, &chamadas);
    printf("Potencia: %.2f\n", pot);
    printf("Chamadas: %d\n", chamadas);
    printf("Fib(K): %d\n", fib(k));
    return 0;
}

int fib(int n) {
    if (n == 0) {
        return 0;
    }
    if (n == 1) {
        return 1;
    }
    return fib(n - 1) + fib(n - 2);
}

double potencia_rapida(double x, int n, int *chamadas) {
    (*chamadas)++;
    if (n == 0) {
        return 1.0;
    }
    if (n == 1) {
        return x;
    }
    double p = potencia_rapida(x, n / 2, chamadas);
    if (n % 2 == 0) {
        return p * p;
    }
    return x * p * p;
}
