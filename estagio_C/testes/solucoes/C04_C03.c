#include <stdio.h>

int main(void) {
    int op, a, b;

    do {
        scanf("%d", &op);
        switch (op) {
            case 1:
                scanf("%d %d", &a, &b);
                printf("Resultado: %d\n", a + b);
                break;
            case 2:
                scanf("%d %d", &a, &b);
                printf("Resultado: %d\n", a * b);
                break;
            case 3:
                scanf("%d", &a);
                do {
                    scanf("%d", &b);
                    if (b == 0) {
                        printf("Divisor invalido\n");
                    }
                } while (b == 0);
                printf("Resultado: %d\n", a / b);
                break;
            case 0:
                printf("Saindo\n");
                break;
            default:
                printf("Opcao invalida\n");
                break;
        }
    } while (op != 0);

    return 0;
}
