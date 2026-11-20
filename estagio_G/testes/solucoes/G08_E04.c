#include <stdio.h>

int fib_contado(int n, int *chamadas);

int main(void) {
    int n, chamadas = 0;
    scanf("%d", &n);

    int f = fib_contado(n, &chamadas);
    printf("Fib: %d\n", f);
    printf("Chamadas: %d\n", chamadas);
    return 0;
}

int fib_contado(int n, int *chamadas) {
    (*chamadas)++;
    if (n == 0) {
        return 0;
    }
    if (n == 1) {
        return 1;
    }
    return fib_contado(n - 1, chamadas) + fib_contado(n - 2, chamadas);
}
