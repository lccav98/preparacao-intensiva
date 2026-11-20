#include <stdio.h>

int main(void) {
    int idade, correntista;
    double renda;

    if (scanf("%d %lf %d", &idade, &renda, &correntista) != 3) {
        return 1;
    }

    if ((idade >= 21 && idade <= 65 && renda >= 2500.00) ||
        (correntista == 1 && idade >= 18 && renda >= 1500.00)) {
        printf("Emprestimo Aprovado\n");
    } else {
        printf("Emprestimo Negado\n");
    }

    return 0;
}
