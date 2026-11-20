/* Checagem A05-C02: Correcao de #define e const */
#include <stdio.h>
#define MAX 40

int main(void) {
    const double TAXA = 12.50;

    printf("Max: %d | Taxa: %.2f\n", MAX, TAXA);
    return 0;
}
