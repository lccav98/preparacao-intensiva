#include <stdio.h>

int main(void) {
    double horas, total;
    scanf("%lf", &horas);

    if (horas <= 1.0) {
        total = 8.00;
    } else if (horas <= 3.0) {
        total = 15.00;
    } else if (horas <= 6.0) {
        total = 24.00;
    } else {
        total = 24.00 + (horas - 6.0) * 4.50;
    }

    printf("Total: R$ %.2f\n", total);
    return 0;
}
