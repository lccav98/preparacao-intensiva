#include <stdio.h>

int main(void) {
    int a, b, c, aux;
    scanf("%d %d %d", &a, &b, &c);

    printf("Antes: %d %d %d\n", a, b, c);

    aux = c;
    c = b;
    b = a;
    a = aux;

    printf("Depois: %d %d %d\n", a, b, c);
    return 0;
}
