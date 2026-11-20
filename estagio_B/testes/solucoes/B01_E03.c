#include <stdio.h>

int main(void) {
    int total_seg, minutos, segundos;
    scanf("%d", &total_seg);

    minutos = total_seg / 60;
    segundos = total_seg % 60;

    printf("Minutos: %d\n", minutos);
    printf("Segundos: %d\n", segundos);
    return 0;
}
