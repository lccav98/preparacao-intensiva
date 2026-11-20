#include <stdio.h>

int main(void) {
    double eps;
    if (scanf("%lf", &eps) != 1) {
        return 1;
    }

    if (eps <= 0.0) {
        printf("Tolerancia Invalida\n");
        return 0;
    }

    double soma = 0.0;
    double termo = 1.0;
    int k = 0;

    while (termo >= eps) {
        soma += termo;
        k++;
        termo = termo / k;
    }

    printf("Soma = %.8f\n", soma);
    printf("Termos = %d\n", k);
    return 0;
}
