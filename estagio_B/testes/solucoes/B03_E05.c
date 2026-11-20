#include <stdio.h>

int main(void) {
    double vel, multa;
    scanf("%lf", &vel);

    if (vel > 80.0) {
        multa = (vel - 80.0) * 5.0;
        printf("Multa: R$ %.2f\n", multa);
    }

    printf("Boa viagem\n");
    return 0;
}
