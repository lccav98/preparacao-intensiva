#include <stdio.h>

int main(void) {
    int x, y;
    scanf("%d %d", &x, &y);

    int *px = &x;
    int *py = &y;

    if (*px > *py) {
        int aux = *px;
        *px = *py;
        *py = aux;
    }

    int iguais = 0;
    if (*px == *py) {
        iguais = 1;
    }

    printf("Iguais: %d\nOrdenados: %d %d\n", iguais, x, y);
    return 0;
}
