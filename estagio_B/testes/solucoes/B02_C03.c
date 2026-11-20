#include <stdio.h>
#include <math.h>

int main(void) {
    int a, b;
    double hipotenusa;
    scanf("%d %d", &a, &b);

    hipotenusa = sqrt((double)(a * a + b * b));

    printf("Hipotenusa: %.2f\n", hipotenusa);
    return 0;
}
