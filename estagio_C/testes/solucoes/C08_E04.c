#include <stdio.h>

int main(void) {
    double x;
    int n;
    if (scanf("%lf %d", &x, &n) != 2) {
        return 1;
    }

    double soma = 0.0;
    double termo = 1.0;

    for (int k = 0; k < n; k++) {
        soma += termo;
        termo = termo * x / (k + 1);
    }

    printf("e^x aprox: %.6f\n", soma);
    return 0;
}
