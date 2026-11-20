#include <stdio.h>

int contar_zeros(int n);

int main(void) {
    int n;
    scanf("%d", &n);
    printf("Zeros: %d\n", contar_zeros(n));
    return 0;
}

int contar_zeros(int n) {
    // Bug original: if (n == 0) return 0; falhava para a entrada 0.
    // Correcao: tratar n < 10 no caso base (0 possui 1 zero; 1..9 possuem 0 zeros).
    if (n < 10) {
        if (n == 0) {
            return 1;
        }
        return 0;
    }
    if (n % 10 == 0) {
        return 1 + contar_zeros(n / 10);
    }
    return contar_zeros(n / 10);
}
