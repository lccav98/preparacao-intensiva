#include <stdio.h>

int main(void) {
    int x, y, aux;
    scanf("%d %d", &x, &y);

    aux = x;
    x = y;
    y = aux;

    printf("x = %d, y = %d\n", x, y);
    return 0;
}
