#include <stdio.h>

int main(void) {
    int a, b;
    int m, n, resto;

    scanf("%d %d", &a, &b);

    m = a;
    n = b;

    while (n != 0) {
        resto = m % n;
        m = n;
        n = resto;
    }

    printf("MDC: %d\n", m);
    return 0;
}
