#include <stdio.h>

int main(void) {
    int a, b, cod;
    scanf("%d %d %d", &a, &b, &cod);

    // Erro 1 original: int *p; *p = b + 5; desreferenciava ponteiro nao inicializado.
    int *p = &b;
    *p = *p + 5;

    int *q = NULL;
    if (cod == 1) {
        q = &a;
    }

    // Erro 2 original: *q = *q + *p; desreferenciava q mesmo quando q == NULL.
    if (q != NULL) {
        *q = *q + *p;
    }

    printf("%d %d\n", a, b);
    return 0;
}
