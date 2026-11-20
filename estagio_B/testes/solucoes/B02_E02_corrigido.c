#include <stdio.h>
#include <math.h>

int main(void) {
    double a, b, c, delta, x1;
    scanf("%lf %lf %lf", &a, &b, &c);

    delta = b * b - 4.0 * a * c;
    x1 = (-b + sqrt(delta)) / (2.0 * a);

    printf("x1 = %.2f\n", x1);
    return 0;
}
