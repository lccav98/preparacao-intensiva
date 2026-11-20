#include <stdio.h>

int main(void) {
    int a, b;
    int soma = 0;
    int i;

    scanf("%d %d", &a, &b);

    for (i = a; i <= b; i++) {
        if (i % 2 == 0) {
            soma += i;
        }
    }

    printf("Soma pares: %d\n", soma);
    printf("Proximo i: %d\n", i);
    return 0;
}
