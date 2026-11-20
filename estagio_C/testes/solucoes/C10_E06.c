#include <stdio.h>

int main(void) {
    double x, eps;
    if (scanf("%lf %lf", &x, &eps) != 2) {
        return 1;
    }

    if (eps <= 0.0) {
        printf("Entrada Invalida\n");
        return 0;
    }

    double soma = 0.0;
    double termo = x;
    int termos = 0;
    int k = 0;

    while (termo >= eps || termo <= -eps) {
        soma += termo;
        termos++;
        k++;
        double fator = (2.0 * k) * (2.0 * k + 1.0);
        termo = -termo * x * x / fator;
    }

    printf("sen(x) aprox: %.6f\n", soma);
    printf("Termos = %d\n", termos);
    return 0;
}
