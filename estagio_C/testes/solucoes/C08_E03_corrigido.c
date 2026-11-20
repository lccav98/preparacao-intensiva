#include <stdio.h>

int main(void) {
    double eps;
    if (scanf("%lf", &eps) != 1) {
        return 1;
    }

    double soma = 0.0;
    double termo = 1.0;
    int k = 1;

    while (termo >= eps) {
        soma += termo;
        k++;
        termo = 1.0 / ((double)k * k);
    }

    printf("Soma = %.6f\n", soma);
    return 0;
}
