#include <stdio.h>

int main(void) {
    int n;
    if (scanf("%d", &n) != 1) {
        return 1;
    }

    double soma = 0.0;
    double fat = 1.0;

    for (int k = 1; k <= n; k++) {
        fat *= k;
        soma += 1.0 / fat;
    }

    printf("Soma = %.6f\n", soma);
    return 0;
}
