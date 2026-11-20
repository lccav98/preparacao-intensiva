#include <stdio.h>

int main(void) {
    double compra, desconto, total;
    scanf("%lf", &compra);

    if (compra < 100.0) {
        desconto = 0.0;
    } else if (compra < 200.0) {
        desconto = compra * 0.05;
    } else if (compra < 300.0) {
        desconto = compra * 0.10;
    } else {
        desconto = compra * 0.15;
    }

    total = compra - desconto;
    printf("Desconto: R$ %.2f\n", desconto);
    printf("Total: R$ %.2f\n", total);
    return 0;
}
