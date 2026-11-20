#include <stdio.h>

int main(void) {
    int cod;

    if (scanf("%d", &cod) != 1) {
        return 1;
    }

    switch (cod) {
        case 1:
        case 2:
        case 3:
            printf("Alimento Nao-Perecivel\n");
            break;

        case 4:
        case 5:
        case 6:
            printf("Alimento Perecivel\n");
            break;

        case 7:
            printf("Vestuario\n");
            break;

        case 8:
        case 9:
        case 10:
            printf("Limpeza\n");
            break;

        default:
            printf("Codigo Invalido\n");
            break;
    }

    return 0;
}
