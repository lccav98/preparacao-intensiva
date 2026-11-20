#include <stdio.h>

int main(void) {
    double nota;
    scanf("%lf", &nota);

    if (nota >= 6.0) {
        printf("Aprovado\n");
    } else {
        printf("Reprovado\n");
    }

    return 0;
}
