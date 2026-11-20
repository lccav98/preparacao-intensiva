#include <stdio.h>

int quadrado(int x);
int soma_quadrados(int a, int b);

int main(void) {
    int u, v, total;
    scanf("%d %d", &u, &v);
    total = soma_quadrados(u, v);
    printf("Soma dos quadrados: %d\n", total);
    return 0;
}

int quadrado(int x) {
    return x * x;
}

int soma_quadrados(int a, int b) {
    int resultado = quadrado(a) + quadrado(b);
    return resultado;
}
