#include <stdio.h>
#define TAXA 0.05

int main(void) {
    double fixo1, vendas1, fixo2, vendas2;
    double com1, com2, total1, total2, aux;

    scanf("%lf %lf", &fixo1, &vendas1);
    scanf("%lf %lf", &fixo2, &vendas2);

    com1 = TAXA * vendas1;
    com2 = TAXA * vendas2;
    total1 = fixo1 + com1;
    total2 = fixo2 + com2;

    aux = total1;
    total1 = total2;
    total2 = aux;

    printf("Comissao 1: R$ %.2f\n", com1);
    printf("Comissao 2: R$ %.2f\n", com2);
    printf("Total 1: R$ %.2f\n", total1);
    printf("Total 2: R$ %.2f\n", total2);
    return 0;
}
