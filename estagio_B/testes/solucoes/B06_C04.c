#include <stdio.h>

int main(void) {
    double cra, renda;

    if (scanf("%lf %lf", &cra, &renda) != 2) {
        return 1;
    }

    if ((cra >= 8.5 && renda <= 1800.00) || (cra >= 9.5)) {
        printf("Bolsa Concedida\n");
    } else {
        printf("Bolsa Nao Concedida\n");
    }

    return 0;
}
