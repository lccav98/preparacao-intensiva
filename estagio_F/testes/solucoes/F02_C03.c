#include <stdio.h>

int eh_primo(int n);
int contar_primos(int ini, int fim);

int main(void) {
    int ini, fim;
    scanf("%d %d", &ini, &fim);
    printf("Primos: %d\n", contar_primos(ini, fim));
    return 0;
}

int eh_primo(int n) {
    if (n <= 1) {
        return 0;
    }
    for (int d = 2; d * d <= n; d++) {
        if (n % d == 0) {
            return 0;
        }
    }
    return 1;
}

int contar_primos(int ini, int fim) {
    int cont = 0;
    for (int n = ini; n <= fim; n++) {
        if (eh_primo(n)) {
            cont++;
        }
    }
    return cont;
}
