#include <stdio.h>

int main(void) {
    double mbps, preco;
    scanf("%lf", &mbps);

    if (mbps <= 20.0) {
        preco = 79.90;
    } else if (mbps <= 100.0) {
        preco = 109.90;
    } else if (mbps <= 300.0) {
        preco = 149.90;
    } else {
        preco = 199.90;
    }

    printf("Plano: R$ %.2f\n", preco);
    return 0;
}
