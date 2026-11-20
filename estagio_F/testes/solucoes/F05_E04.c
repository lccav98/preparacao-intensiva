#include <stdio.h>

void soma_e_diferenca(int a, int b, int *soma, int *dif);

int main(void) {
    int a, b, s, d;
    scanf("%d %d", &a, &b);
    soma_e_diferenca(a, b, &s, &d);
    printf("Soma: %d\nDiferenca: %d\n", s, d);
    return 0;
}

void soma_e_diferenca(int a, int b, int *soma, int *dif) {
    *soma = a + b;
    *dif = a - b;
}
