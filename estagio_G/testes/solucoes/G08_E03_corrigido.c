#include <stdio.h>

int fib(int n);
double potencia_rapida(double x, int n, int *chamadas);

int main(void) {
    double x;
    int n, k, chamadas = 0;
    scanf("%lf %d %d", &x, &n, &k);

    double res = potencia_rapida(x, n, &chamadas);
    printf("Potencia: %.2f\n", res);
    printf("Chamadas: %d\n", chamadas);
    printf("Fib: %d\n", fib(k));
    return 0;
}

int fib(int n) {
    if (n == 0) {
        return 0;
    }
    // Erro original 1: faltava o segundo caso base (n == 1), causando recursao infinita para n >= 1.
    // Correcao: retornar 1 quando n == 1.
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
    // Erro original 2: chamava potencia_rapida(x, n / 2, chamadas) duas vezes, destruindo o ganho logaritmico.
    // Correcao: guardar o retorno em uma unica variavel local p.
    double p = potencia_rapida(x, n / 2, chamadas);
    if (n % 2 == 0) {
        return p * p;
    }
    // Erro original 3: no caso impar retornava x * p em vez de x * p * p.
    // Correcao: multiplicar x * p * p quando n eh impar.
    return x * p * p;
}
