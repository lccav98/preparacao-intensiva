#include <stdio.h>

int main(void) {
    int a, b;
    int quociente = 0;
    int resto;

    scanf("%d %d", &a, &b);

    resto = a;
    while (resto >= b) {
        resto = resto - b;
        quociente++;
    }

    printf("Quociente: %d\n", quociente);
    printf("Resto: %d\n", resto);
    return 0;
}
