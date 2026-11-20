#include <stdio.h>

int contar_digitos(int n) {
    if (n == 0) {
        return 1;
    }
    int cont = 0;
    while (n > 0) {
        cont++;
        n /= 10;
    }
    return cont;
}

int soma_digitos(int n) {
    int soma = 0;
    while (n > 0) {
        soma += n % 10;
        n /= 10;
    }
    return soma;
}

int main(void) {
    int n;
    scanf("%d", &n);
    printf("Digitos: %d\n", contar_digitos(n));
    printf("Soma dos digitos: %d\n", soma_digitos(n));
    return 0;
}
