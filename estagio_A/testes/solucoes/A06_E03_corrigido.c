#include <stdio.h>

int main(void) {
    int item;
    double preco;
    char setor;

    scanf("%d", &item);
    scanf("%lf", &preco);
    scanf(" %c", &setor);

    printf("Item: %d\n", item);
    printf("Preco: R$ %.2f\n", preco);
    printf("Setor: %c\n", setor);
    return 0;
}
