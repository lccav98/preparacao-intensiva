#include <stdio.h>

int main(void) {
    int valor;
    double desconto;
    scanf("%d", &valor);

    desconto = (10.0 / 100.0) * valor;

    printf("Desconto: R$ %.2f\n", desconto);
    return 0;
}
