#include <stdio.h>

int main(void) {
    int saldo, bonus, taxa;
    scanf("%d %d %d", &saldo, &bonus, &taxa);

    saldo += bonus;
    saldo -= taxa;
    saldo *= 2;
    saldo++;

    printf("Saldo final: %d\n", saldo);
    return 0;
}
