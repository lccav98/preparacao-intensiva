#include <stdio.h>

int main(void) {
    double peso, taxa;
    scanf("%lf", &peso);

    if (peso <= 10.0) {
        taxa = 0.00;
    } else if (peso <= 20.0) {
        taxa = 40.00;
    } else if (peso <= 30.0) {
        taxa = 75.00;
    } else {
        taxa = 75.00 + (peso - 30.0) * 8.50;
    }

    printf("Taxa: R$ %.2f\n", taxa);
    return 0;
}
