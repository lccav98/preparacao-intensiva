#include <stdio.h>

int main(void) {
    int dividendo, divisor;
    int quociente = 0;
    int resto;

    scanf("%d %d", &dividendo, &divisor);

    resto = dividendo;
    while (resto >= divisor) {
        resto -= divisor;
        quociente++;
    }

    printf("Quociente: %d\n", quociente);
    printf("Resto: %d\n", resto);
    return 0;
}
