#include <stdio.h>

int main(void) {
    int a, b;
    int resto;
    scanf("%d %d", &a, &b);

    resto = a;
    while (resto >= b) {
        resto -= b;
    }

    printf("Resto: %d\n", resto);
    return 0;
}
