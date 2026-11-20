#include <stdio.h>

int main(void) {
    int freq;
    double nota;

    if (scanf("%d %lf", &freq, &nota) != 2) {
        return 1;
    }

    if (freq < 75) {
        printf("Reprovado por Falta\n");
    } else {
        if (nota >= 7.0) {
            printf("Aprovado\n");
        } else if (nota >= 4.0) {
            printf("Exame Final\n");
        } else {
            printf("Reprovado por Nota\n");
        }
    }

    return 0;
}
