#include <stdio.h>

int main(void) {
    double alt;
    int idade;

    if (scanf("%lf %d", &alt, &idade) != 2) {
        return 1;
    }

    if ((alt >= 1.50 && idade >= 12) || (idade >= 16 && alt >= 1.40)) {
        printf("Acesso Permitido\n");
    } else {
        printf("Acesso Negado\n");
    }

    return 0;
}
