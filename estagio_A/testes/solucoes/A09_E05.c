#include <stdio.h>

int main(void) {
    float af = 0.1f, bf = 0.2f, sf = af + bf;
    double ad = 0.1, bd = 0.2, sd = ad + bd;

    printf("float 10 casas: %.10f\n", sf);
    printf("float 20 casas: %.20f\n", sf);
    printf("double 10 casas: %.10f\n", sd);
    printf("double 20 casas: %.20f\n", sd);
    return 0;
}
