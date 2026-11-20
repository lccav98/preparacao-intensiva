#include <stdio.h>

int main(void) {
    int p, q, r, aux;
    scanf("%d %d %d", &p, &q, &r);

    aux = p;
    p = q;
    q = r;
    r = aux;

    printf("Resultado: %d %d %d\n", p, q, r);
    return 0;
}
