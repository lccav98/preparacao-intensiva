#include <stdio.h>

int produto_digitos(int n);
int maior_digito(int n);

int main(void) {
    int n;
    scanf("%d", &n);
    printf("Produto: %d\n", produto_digitos(n));
    printf("Maior digito: %d\n", maior_digito(n));
    return 0;
}

int produto_digitos(int n) {
    if (n < 10) {
        return n;
    }
    return (n % 10) * produto_digitos(n / 10);
}

int maior_digito(int n) {
    if (n < 10) {
        return n;
    }
    int ult = n % 10;
    int resto = maior_digito(n / 10);
    if (ult > resto) {
        return ult;
    }
    return resto;
}
