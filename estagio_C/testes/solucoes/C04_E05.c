#include <stdio.h>

int main(void) {
    int total = 0;
    int opcao, v;

    do {
        scanf("%d", &opcao);
        switch (opcao) {
            case 1:
                scanf("%d", &v);
                total += v;
                printf("Total: %d\n", total);
                break;
            case 2:
                scanf("%d", &v);
                total -= v;
                printf("Total: %d\n", total);
                break;
            case 3:
                total = 0;
                printf("Total: %d\n", total);
                break;
            case 0:
                printf("Final: %d\n", total);
                break;
            default:
                printf("Opcao invalida\n");
                break;
        }
    } while (opcao != 0);

    return 0;
}
