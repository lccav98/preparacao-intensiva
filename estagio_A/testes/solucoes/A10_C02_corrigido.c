#include <stdio.h>
#define TAXA 0.10

int main(void) {
    double valor, acrescimo;
    scanf("%lf", &valor);
    acrescimo = valor * TAXA;
    printf("Taxa aplicada: \"10%%\"\nValor final: R$ %.2f\n", valor + acrescimo);
    return 0;
}
