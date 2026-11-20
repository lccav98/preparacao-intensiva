#include <stdio.h>
#define BONUS 50.0

int main(void) {
    double salario_base, salario_final;
    scanf("%lf", &salario_base);
    salario_final = salario_base + BONUS;
    printf("Total: R$ %.2f\n", salario_final);
    return 0;
}
