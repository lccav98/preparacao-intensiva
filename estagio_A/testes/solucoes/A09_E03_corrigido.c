#include <stdio.h>

int main(void) {
    float a = 0.1f;
    double b = 0.1;

    printf("float: %zu bytes\n", sizeof(float));
    printf("double: %zu bytes\n", sizeof(double));
    printf("float 0.1f (10 casas): %.10f\n", a);
    printf("float 0.1f (20 casas): %.20f\n", a);
    printf("double 0.1 (10 casas): %.10f\n", b);
    printf("double 0.1 (20 casas): %.20f\n", b);
    return 0;
}
