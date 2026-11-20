#include <stdio.h>
#include <math.h>

int main(void) {
    double a, b, c, delta, x1, x2;
    scanf("%lf %lf %lf", &a, &b, &c);

    delta = b * b - 4.0 * a * c;
    x1 = (-b + sqrt(delta)) / (2.0 * a);
    x2 = (-b - sqrt(delta)) / (2.0 * a);

    printf("x1 = %.2f\n", x1);
    printf("x2 = %.2f\n", x2);
    return 0;
}
