#include <stdio.h>

int main(void) {
    double dist, taxa;
    scanf("%lf", &dist);

    if (dist <= 5.0) {
        taxa = 10.00;
    } else if (dist <= 15.0) {
        taxa = 18.00;
    } else if (dist <= 30.0) {
        taxa = 28.00;
    } else {
        taxa = 28.00 + (dist - 30.0) * 2.25;
    }

    printf("Taxa: R$ %.2f\n", taxa);
    return 0;
}
