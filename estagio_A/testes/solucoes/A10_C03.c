#include <stdio.h>

int main(void) {
    const double COMISSAO = 0.05;
    double lado_a, lado_b, preco_m2, area, comissao, aux;

    scanf("%lf %lf %lf", &lado_a, &lado_b, &preco_m2);

    area = lado_a * lado_b;
    comissao = area * preco_m2 * COMISSAO;

    aux = lado_a;
    lado_a = lado_b;
    lado_b = aux;

    printf("Dimensoes trocadas: %.2f x %.2f\n", lado_a, lado_b);
    printf("Area: %.2f m2\n", area);
    printf("Comissao: R$ %.2f\n", comissao);
    return 0;
}
