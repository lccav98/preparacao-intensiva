#include <stdio.h>

int main(void) {
    double salario_bruto;
    int dependentes;

    if (scanf("%lf %d", &salario_bruto, &dependentes) != 2) {
        return 1;
    }

    if (salario_bruto <= 0.0 || dependentes < 0) {
        printf("Entrada Invalida\n");
    } else {
        double inss;
        if (salario_bruto <= 1412.00) {
            inss = salario_bruto * 0.075;
        } else if (salario_bruto <= 2666.00) {
            inss = salario_bruto * 0.09;
        } else if (salario_bruto <= 4000.00) {
            inss = salario_bruto * 0.12;
        } else {
            inss = 550.00;
        }

        double base_irrf = salario_bruto - inss - (dependentes * 189.59);
        if (base_irrf < 0.0) {
            base_irrf = 0.0;
        }

        double irrf;
        if (base_irrf <= 2259.20) {
            irrf = 0.0;
        } else if (base_irrf <= 2826.65) {
            irrf = base_irrf * 0.075;
        } else if (base_irrf <= 3751.05) {
            irrf = base_irrf * 0.15;
        } else {
            irrf = base_irrf * 0.225;
        }

        double liquido = salario_bruto - inss - irrf;

        printf("INSS: R$ %.2f\n", inss);
        printf("IRRF: R$ %.2f\n", irrf);
        printf("Liquido: R$ %.2f\n", liquido);
    }

    return 0;
}
