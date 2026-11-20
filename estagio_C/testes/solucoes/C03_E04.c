#include <stdio.h>

int main(void) {
    double valor;
    double soma = 0.0;
    int qtd = 0;

    scanf("%lf", &valor);

    while (valor > 0.0) {
        soma += valor;
        qtd++;
        scanf("%lf", &valor);
    }

    if (qtd > 0) {
        printf("Media: %.2f\n", soma / qtd);
    } else {
        printf("Nenhum positivo lido\n");
    }

    return 0;
}
