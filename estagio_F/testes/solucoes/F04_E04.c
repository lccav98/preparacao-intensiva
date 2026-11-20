#include <stdio.h>

int main(void) {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);

    int *p_menor = &a;
    int *p_maior = &a;

    if (b < *p_menor) {
        p_menor = &b;
    }
    if (c < *p_menor) {
        p_menor = &c;
    }
    if (b > *p_maior) {
        p_maior = &b;
    }
    if (c > *p_maior) {
        p_maior = &c;
    }

    *p_menor = *p_menor + 10;
    printf("Valores: %d %d %d\nApontado por p_maior: %d\n", a, b, c, *p_maior);
    return 0;
}
