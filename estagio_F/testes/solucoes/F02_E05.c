#include <stdio.h>

int soma_divisores_proprios(int n);
int eh_perfeito(int n);

int main(void) {
    int a, b, soma = 0;
    scanf("%d %d", &a, &b);
    for (int n = a; n <= b; n++) {
        if (eh_perfeito(n)) {
            soma++;
        }
    }
    printf("Perfeitos: %d\n", soma);
    return 0;
}

int soma_divisores_proprios(int n) {
    int soma = 0;
    for (int i = 1; i <= n / 2; i++) {
        if (n % i == 0) {
            soma += i;
        }
    }
    return soma;
}

int eh_perfeito(int n) {
    if (n <= 1) {
        return 0;
    }
    if (soma_divisores_proprios(n) == n) {
        return 1;
    }
    return 0;
}
