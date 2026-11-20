#include <stdio.h>

int main(void) {
    int sala;
    double area;

    scanf("%d", &sala);
    scanf("%lf", &area);

    printf("Sala: %d\n", sala);
    printf("Area: %.2f m2\n", area);
    return 0;
}
