#include <stdio.h>

int main(void) {
    double a, b;
    int escolha;
    scanf("%lf %lf %d", &a, &b, &escolha);

    double *alvo = NULL;
    if (escolha == 1) {
        alvo = &a;
    } else if (escolha == 2) {
        alvo = &b;
    }

    if (alvo != NULL) {
        *alvo = (*alvo) * 1.10;
        printf("Atualizado: %.2f\n", *alvo);
    } else {
        printf("Ponteiro nulo\n");
    }
    printf("Valores: %.2f %.2f\n", a, b);
    return 0;
}
