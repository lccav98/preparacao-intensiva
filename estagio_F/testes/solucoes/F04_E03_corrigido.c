#include <stdio.h>

int main(void) {
    int x, y;
    scanf("%d %d", &x, &y);

    // Erro 1 original: int *p; *p = x * 2; desreferenciava ponteiro nao inicializado.
    int *p = &x;
    *p = (*p) * 2;

    int *q = NULL;
    if (y > 0) {
        // Erro 2 original: q = y; atribuia um int ao ponteiro em vez do endereco &y.
        q = &y;
    }

    // Erro 3 original: *p = *p + *q; desreferenciava q mesmo quando q == NULL.
    if (q != NULL) {
        *p = *p + *q;
    }

    printf("%d\n", x);
    return 0;
}
