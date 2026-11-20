#include <stdio.h>

int main(void) {
    int dia, mes, ano;

    if (scanf("%d %d %d", &dia, &mes, &ano) != 3) {
        return 1;
    }

    if (ano <= 0 || mes < 1 || mes > 12) {
        printf("Data Invalida\n");
    } else {
        int bissexto = ((ano % 4 == 0 && ano % 100 != 0) || (ano % 400 == 0));
        int limite_dias;

        if (mes == 2) {
            if (bissexto) {
                limite_dias = 29;
            } else {
                limite_dias = 28;
            }
        } else if (mes == 4 || mes == 6 || mes == 9 || mes == 11) {
            limite_dias = 30;
        } else {
            limite_dias = 31;
        }

        if (dia >= 1 && dia <= limite_dias) {
            if (bissexto) {
                printf("Data Valida: Bissexto\n");
            } else {
                printf("Data Valida: Nao Bissexto\n");
            }
        } else {
            printf("Data Invalida\n");
        }
    }

    return 0;
}
