#include <stdio.h>

double calcular_subtotal(double preco, int qtd) {
    return preco * qtd;
}

double calcular_desconto(double total) {
    if (total >= 200.0) {
        return total * 0.10;
    }
    return 0.0;
}

int main(void) {
    double preco, subtotal, desc;
    int qtd;
    scanf("%lf %d", &preco, &qtd);
    subtotal = calcular_subtotal(preco, qtd);
    desc = calcular_desconto(subtotal);
    printf("Total: %.2f\n", subtotal - desc);
    return 0;
}
