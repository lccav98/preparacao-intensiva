#include <stdio.h>

int contar_digitos(int n);
int soma_digitos(int n);
double potencia_rapida(double x, int n);

int main(void) {
    int num, exp;
    double x;
    scanf("%d %lf %d", &num, &x, &exp);

    printf("Digitos: %d\n", contar_digitos(num));
    printf("Soma digitos: %d\n", soma_digitos(num));
    printf("Potencia: %.2f\n", potencia_rapida(x, exp));
    return 0;
}

int contar_digitos(int n) {
    if (n < 10) {
        return 1;
    }
    return 1 + contar_digitos(n / 10);
}

int soma_digitos(int n) {
    if (n == 0) {
        return 0;
    }
    return (n % 10) + soma_digitos(n / 10);
}

double potencia_rapida(double x, int n) {
    if (n == 0) {
        return 1.0;
    }
    if (n == 1) {
        return x;
    }
    double p = potencia_rapida(x, n / 2);
    if (n % 2 == 0) {
        return p * p;
    }
    return x * p * p;
}
