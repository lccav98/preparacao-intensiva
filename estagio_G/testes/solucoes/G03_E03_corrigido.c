#include <stdio.h>

int contar_digitos(int n);
int potencia(int x, int e);

int main(void) {
    int n, x, e;
    scanf("%d %d %d", &n, &x, &e);
    printf("Digitos: %d\n", contar_digitos(n));
    printf("Potencia: %d\n", potencia(x, e));
    return 0;
}

int contar_digitos(int n) {
    // Bug 1 original: if (n == 0) return 0; retornava 0 para a entrada 0.
    // Correcao: qualquer inteiro 0..9 tem 1 digito.
    if (n < 10) {
        return 1;
    }
    return 1 + contar_digitos(n / 10);
}

int potencia(int x, int e) {
    // Bug 2 original: utilizava laco while em funcao que deve ser recursiva.
    if (e == 0) {
        return 1;
    }
    return x * potencia(x, e - 1);
}
