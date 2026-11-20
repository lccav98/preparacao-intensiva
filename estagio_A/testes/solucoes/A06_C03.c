#include <stdio.h>

int main(void) {
    int id;
    double valor;
    char situacao;

    scanf("%d %lf %c", &id, &valor, &situacao);

    printf("ID: %d\n", id);
    printf("Valor: R$ %.2f\n", valor);
    printf("Situacao: %c\n", situacao);
    return 0;
}
