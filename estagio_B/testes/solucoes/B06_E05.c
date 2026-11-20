#include <stdio.h>

int main(void) {
    double a, b, c;

    if (scanf("%lf %lf %lf", &a, &b, &c) != 3) {
        return 1;
    }

    if (a < b + c && b < a + c && c < a + b) {
        printf("Triangulo Valido\n");
    } else {
        printf("Triangulo Invalido\n");
    }

    return 0;
}
