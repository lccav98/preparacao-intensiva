#include <stdio.h>

int main(void) {
    int codigo;
    double temperatura;
    char escala;

    scanf("%d %lf %c", &codigo, &temperatura, &escala);

    printf("Sensor %d: %.1f %c\n", codigo, temperatura, escala);
    return 0;
}
