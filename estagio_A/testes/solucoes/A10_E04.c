#include <stdio.h>

int main(void) {
    const double FATOR_PERIMETRO = 2.0;
    double largura, comprimento, area, perimetro;

    scanf("%lf %lf", &largura, &comprimento);

    area = largura * comprimento;
    perimetro = FATOR_PERIMETRO * (largura + comprimento);

    printf("Area: %.2f m2\n", area);
    printf("Perimetro: %.2f m\n", perimetro);
    return 0;
}
