#include <stdio.h>

int main(void) {
    int tempo_seg, h, m, s, resto;
    scanf("%d", &tempo_seg);

    h = tempo_seg / 3600;
    resto = tempo_seg % 3600;
    m = resto / 60;
    s = resto % 60;

    printf("Horas: %d\n", h);
    printf("Minutos: %d\n", m);
    printf("Segundos: %d\n", s);
    return 0;
}
