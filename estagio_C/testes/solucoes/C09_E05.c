#include <stdio.h>

int main(void) {
    int dias, inicio;
    if (scanf("%d %d", &dias, &inicio) != 2) {
        return 1;
    }

    if (dias < 28 || dias > 31 || inicio < 1 || inicio > 7) {
        printf("Entrada Invalida\n");
        return 0;
    }

    printf("Dom Seg Ter Qua Qui Sex Sab\n");

    for (int i = 1; i < inicio; i++) {
        printf("    ");
    }

    for (int d = 1; d <= dias; d++) {
        printf("%3d", d);
        if ((inicio - 1 + d) % 7 == 0 || d == dias) {
            printf("\n");
        } else {
            printf(" ");
        }
    }

    return 0;
}
