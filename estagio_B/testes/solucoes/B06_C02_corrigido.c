#include <stdio.h>

int main(void) {
    double nota;
    int freq;

    if (scanf("%lf %d", &nota, &freq) != 2) {
        return 1;
    }

    if (nota >= 6.0 && nota <= 10.0 && freq >= 75) {
        printf("Aprovado\n");
    } else {
        printf("Reprovado\n");
    }

    return 0;
}
