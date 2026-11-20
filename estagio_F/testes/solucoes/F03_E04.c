#include <stdio.h>

int processar_saque(int saldo, int valor);

int main(void) {
    int saldo, saque, novo_saldo;
    scanf("%d %d", &saldo, &saque);
    novo_saldo = processar_saque(saldo, saque);
    printf("Original: %d\nAtualizado: %d\n", saldo, novo_saldo);
    return 0;
}

int processar_saque(int saldo, int valor) {
    if (valor > 0 && valor <= saldo) {
        saldo -= valor;
    }
    return saldo;
}
