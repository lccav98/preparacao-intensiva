#include <stdio.h>

int main(void) {
    double temp;
    scanf("%lf", &temp);

    if (temp >= 37.8) {
        printf("Estado febril: %.1f C\n", temp);
    } else {
        printf("Temperatura normal: %.1f C\n", temp);
    }

    return 0;
}
