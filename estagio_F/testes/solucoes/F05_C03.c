#include <stdio.h>

void retangulo(double base, double altura, double *area, double *perimetro);

int main(void) {
    double base, altura, area, perimetro;
    scanf("%lf %lf", &base, &altura);
    retangulo(base, altura, &area, &perimetro);
    printf("Area: %.2f\nPerimetro: %.2f\n", area, perimetro);
    return 0;
}

void retangulo(double base, double altura, double *area, double *perimetro) {
    *area = base * altura;
    *perimetro = 2.0 * (base + altura);
}
