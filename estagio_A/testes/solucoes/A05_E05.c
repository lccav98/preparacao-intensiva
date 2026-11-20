/* Exercicio A05-E05: Ficha formatada de produto */
#include <stdio.h>

int main(void) {
    const int ANO_BASE = 2026;
    int codigo = 308;
    double valorUnitario = 49.876;
    double peso = 7.2;
    char setor = 'E';

    printf("Ficha %d - Setor %c\n", ANO_BASE, setor);
    printf("Codigo: %d\n", codigo);
    printf("Valor: R$ %.2f\n", valorUnitario);
    printf("Peso: %.1f kg\n", peso);
    return 0;
}
