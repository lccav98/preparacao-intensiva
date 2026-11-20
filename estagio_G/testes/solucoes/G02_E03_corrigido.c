#include <stdio.h>

void espelho(int n);

int main(void) {
    int n;
    scanf("%d", &n);
    espelho(n);
    printf("\n");
    return 0;
}

void espelho(int n) {
    // Bug 1 original: faltava caso base (if (n <= 0) return;), causando stack overflow.
    if (n <= 0) {
        return;
    }
    // Pre-recursao (descida): imprime de n ate 1.
    printf("%d ", n);
    espelho(n - 1);
    // Bug 2 original: o segundo bloco de impressao estava antes da chamada recursiva.
    // Pos-recursao (subida): imprime de 1 ate n na volta da pilha.
    if (n > 1) {
        printf(" ");
    }
    printf("%d", n);
}
