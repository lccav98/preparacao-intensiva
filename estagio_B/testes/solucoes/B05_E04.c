#include <stdio.h>

int main(void) {
    double kwh, total;
    scanf("%lf", &kwh);

    if (kwh <= 100.0) {
        total = kwh * 0.50;
    } else if (kwh <= 250.0) {
        total = kwh * 0.65;
    } else {
        total = kwh * 0.80;
    }

    printf("Total: R$ %.2f\n", total);
    return 0;
}
