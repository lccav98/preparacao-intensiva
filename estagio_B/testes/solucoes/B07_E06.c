#include <stdio.h>

int main(void) {
    double renda_mensal, valor_parcela;
    int restricoes_spc;

    if (scanf("%lf %lf %d", &renda_mensal, &valor_parcela, &restricoes_spc) != 3) {
        return 1;
    }

    if (restricoes_spc != 0) {
        printf("Credito Recusado: Restricao Cadastral\n");
    } else {
        if (valor_parcela <= renda_mensal * 0.30) {
            printf("Credito Aprovado\n");
        } else {
            printf("Credito Recusado: Parcela Excede Margem\n");
        }
    }

    return 0;
}
