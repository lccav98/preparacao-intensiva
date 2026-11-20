#include <stdio.h>
#include <math.h>

int main(void) {
    double a, b, c;

    if (scanf("%lf %lf %lf", &a, &b, &c) != 3) {
        return 1;
    }

    if (a < b + c && b < a + c && c < a + b) {
        double s = (a + b + c) / 2.0;
        double area = sqrt(s * (s - a) * (s - b) * (s - c));

        if (a == b && b == c) {
            printf("Equilatero - Area: %.2f\n", area);
        } else if (a == b || a == c || b == c) {
            printf("Isosceles - Area: %.2f\n", area);
        } else {
            printf("Escaleno - Area: %.2f\n", area);
        }
    } else {
        printf("Invalido\n");
    }

    return 0;
}
