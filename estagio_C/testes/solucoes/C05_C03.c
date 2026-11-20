#include <stdio.h>

int main(void) {
    int n;
    int qtd_par_ou_m7 = 0;
    int soma_impares_gt5 = 0;
    int soma_total = 0;

    scanf("%d", &n);

    if (n <= 0) {
        printf("Entrada invalida\n");
    } else {
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 0 || i % 7 == 0) {
                qtd_par_ou_m7++;
            }
            if (i % 2 != 0 && i > 5) {
                soma_impares_gt5 += i;
            }
            soma_total += i;
        }

        printf("Qtd par ou mult7: %d\n", qtd_par_ou_m7);
        printf("Soma impares > 5: %d\n", soma_impares_gt5);
        printf("Media total: %.2f\n", (double)soma_total / n);
    }

    return 0;
}
