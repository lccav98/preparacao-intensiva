#include <stdio.h>
#include <math.h>

int main(void) {
    double a, b, c;

    if (scanf("%lf %lf %lf", &a, &b, &c) != 3) {
        return 1;
    }

    if (a == 0.0) {
        printf("Nao e equacao de segundo grau\n");
    } else {
        double delta = b * b - 4.0 * a * c;
        if (delta < 0.0) {
            printf("Sem raizes reais\n");
        } else if (delta == 0.0) {
            double x = -b / (2.0 * a);
            printf("Raiz unica: %.2f\n", x);
        } else {
            double x1 = (-b + sqrt(delta)) / (2.0 * a);
            double x2 = (-b - sqrt(delta)) / (2.0 * a);
            printf("Raizes: %.2f e %.2f\n", x1, x2);
        }
    }

    return 0;
}
