#include <stdio.h>
#include "calc.h"

int main(void) {
    int a, b;
    scanf("%d %d", &a, &b);
    printf("Soma: %d\n", soma_intervalo(a, b));
    printf("Pares: %d\n", contar_pares(a, b));
    return 0;
}
