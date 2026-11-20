#include <stdio.h>

int contar_digitos_maiores(int n, int lim);
int potencia(int x, int e);

int main(void) {
    int n, lim, x, e;
    scanf("%d %d %d %d", &n, &lim, &x, &e);
    printf("Maiores que lim: %d\n", contar_digitos_maiores(n, lim));
    printf("Potencia: %d\n", potencia(x, e));
    return 0;
}

int contar_digitos_maiores(int n, int lim) {
    if (n < 10) {
        if (n > lim) {
            return 1;
        }
        return 0;
    }
    if (n % 10 > lim) {
        return 1 + contar_digitos_maiores(n / 10, lim);
    }
    return contar_digitos_maiores(n / 10, lim);
}

int potencia(int x, int e) {
    if (e == 0) {
        return 1;
    }
    return x * potencia(x, e - 1);
}
