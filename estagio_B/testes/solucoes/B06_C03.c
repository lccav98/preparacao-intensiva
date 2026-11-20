#include <stdio.h>

int main(void) {
    int dia, mes;

    if (scanf("%d %d", &dia, &mes) != 2) {
        return 1;
    }

    if (mes == 2 && dia >= 1 && dia <= 28) {
        printf("Data Valida\n");
    } else if ((mes == 4 || mes == 6 || mes == 9 || mes == 11) && (dia >= 1 && dia <= 30)) {
        printf("Data Valida\n");
    } else if ((mes == 1 || mes == 3 || mes == 5 || mes == 7 || mes == 8 || mes == 10 || mes == 12) && (dia >= 1 && dia <= 31)) {
        printf("Data Valida\n");
    } else {
        printf("Data Invalida\n");
    }

    return 0;
}
