#include <stdio.h>

int main(void) {
    int nota;
    int qtd = 0;
    double soma = 0.0;

    while (1) {
        if (scanf("%d", &nota) != 1) {
            break;
        }
        if (nota < 0) {
            break;
        }
        soma += nota;
        qtd++;
    }

    if (qtd == 0) {
        printf("Nenhuma nota valida\n");
    } else {
        printf("Qtd: %d\n", qtd);
        printf("Media: %.2f\n", soma / qtd);
    }

    return 0;
}
