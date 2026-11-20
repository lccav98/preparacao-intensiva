#include <stdio.h>

int eh_bissexto(int ano);
int dias_no_mes(int mes, int ano);

int main(void) {
    int mes, ano, dias;
    scanf("%d %d", &mes, &ano);
    dias = dias_no_mes(mes, ano);
    if (dias < 0) {
        printf("Mes invalido\n");
    } else {
        printf("Dias: %d\n", dias);
    }
    return 0;
}

int eh_bissexto(int ano) {
    if ((ano % 400 == 0) || (ano % 4 == 0 && ano % 100 != 0)) {
        return 1;
    }
    return 0;
}

int dias_no_mes(int mes, int ano) {
    switch (mes) {
        case 1: case 3: case 5: case 7: case 8: case 10: case 12:
            return 31;
        case 4: case 6: case 9: case 11:
            return 30;
        case 2:
            if (eh_bissexto(ano)) {
                return 29;
            }
            return 28;
        default:
            return -1;
    }
}
