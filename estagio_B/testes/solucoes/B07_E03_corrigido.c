#include <stdio.h>

int main(void) {
    int cracha, biometria;

    if (scanf("%d %d", &cracha, &biometria) != 2) {
        return 1;
    }

    if (cracha == 1) {
        if (biometria == 1) {
            printf("Acesso Liberado\n");
        } else {
            printf("Biometria Obrigatoria\n");
        }
    } else {
        printf("Cracha Invalido\n");
    }

    return 0;
}
