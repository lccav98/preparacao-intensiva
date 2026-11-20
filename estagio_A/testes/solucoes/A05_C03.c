/* Checagem A05-C03: Programa completo com constante e especificadores */
#include <stdio.h>
#define VERSAO 3

int main(void) {
    const double TARIFA = 6.258;
    int sala = 102;
    char bloco = 'C';

    printf("Sistema v%d\n", VERSAO);
    printf("Sala %d - Bloco %c\n", sala, bloco);
    printf("Tarifa: R$ %.2f\n", TARIFA);
    return 0;
}
