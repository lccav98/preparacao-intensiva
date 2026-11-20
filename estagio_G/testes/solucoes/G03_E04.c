#include <stdio.h>

int contar_digitos(int n);
int soma_digitos_pares(int n);

int main(void) {
    int n;
    scanf("%d", &n);
    printf("Digitos: %d\n", contar_digitos(n));
    printf("Soma digitos pares: %d\n", soma_digitos_pares(n));
    return 0;
}

int contar_digitos(int n) {
    if (n < 10) {
        return 1;
    }
    return 1 + contar_digitos(n / 10);
}

int soma_digitos_pares(int n) {
    if (n < 10) {
        if (n % 2 == 0) {
            return n;
        }
        return 0;
    }
    int d = n % 10;
    if (d % 2 == 0) {
        return d + soma_digitos_pares(n / 10);
    }
    return soma_digitos_pares(n / 10);
}
