#include <stdio.h>

int main(void) {
    long long n;
    if (scanf("%lld", &n) != 1 || n <= 0) {
        printf("Valor Invalido\n");
        return 0;
    }

    long long temp = n;
    int soma = 0;
    int digitos = 0;

    while (temp > 0) {
        soma += (int)(temp % 10);
        digitos++;
        temp /= 10;
    }

    printf("Soma = %d\n", soma);
    printf("Digitos = %d\n", digitos);

    return 0;
}
