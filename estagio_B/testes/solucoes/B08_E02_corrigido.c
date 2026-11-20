#include <stdio.h>

int main(void) {
    int tipo;

    if (scanf("%d", &tipo) != 1) {
        return 1;
    }

    switch (tipo) {
        case 1:
            printf("Tarifa A\n");
            break;
        case 2:
            printf("Tarifa B\n");
            break;
        default:
            printf("Tarifa Padrao\n");
            break;
    }

    return 0;
}
