#include <stdio.h>

void acumular(int *total, int valor);

int main(void) {
    int saldo = 100, x, y;
    scanf("%d %d", &x, &y);
    acumular(&saldo, x);
    acumular(&saldo, y);
    printf("Saldo: %d\n", saldo);
    return 0;
}

void acumular(int *total, int valor) {
    *total = *total + valor;
}
