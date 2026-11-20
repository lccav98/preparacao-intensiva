#include <stdio.h>

int main(void) {
    int setor, ramal;

    if (scanf("%d %d", &setor, &ramal) != 2) {
        return 1;
    }

    switch (setor) {
        case 1:
            switch (ramal) {
                case 1:
                    printf("Hardware\n");
                    break;
                case 2:
                    printf("Software\n");
                    break;
                default:
                    printf("Ramal Invalido\n");
                    break;
            }
            break;

        case 2:
            switch (ramal) {
                case 1:
                    printf("Contas a Pagar\n");
                    break;
                case 2:
                    printf("Contas a Receber\n");
                    break;
                default:
                    printf("Ramal Invalido\n");
                    break;
            }
            break;

        default:
            printf("Setor Invalido\n");
            break;
    }

    return 0;
}
