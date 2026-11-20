#include <stdio.h>

double reajustar(double sal, double pct);

int main(void) {
    double salario, percentual;
    scanf("%lf %lf", &salario, &percentual);
    // Erro original: reajustar era void e alterava apenas a copia local 'sal'.
    // Correcao: retornar o novo valor e atribuir a 'salario' em main.
    salario = reajustar(salario, percentual);
    printf("Novo salario: %.2f\n", salario);
    return 0;
}

double reajustar(double sal, double pct) {
    return sal * (1.0 + pct / 100.0);
}
