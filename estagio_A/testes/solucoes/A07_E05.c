#include <stdio.h>

int main(void) {
    double a, b, aux;
    scanf("%lf %lf", &a, &b);

    printf("Antes: a = %.2f, b = %.2f\n", a, b);

    aux = a;
    a = b;
    b = aux;

    printf("Depois: a = %.2f, b = %.2f\n", a, b);
    return 0;
}
