#include <stdio.h>

int main(void) {
    int n;
    if (scanf("%d", &n) != 1) {
        return 1;
    }

    int soma = 0;
    for (int i = 1; i <= n; i += 2) {
        soma += i;
    }

    printf("Soma = %d\n", soma);
    return 0;
}
