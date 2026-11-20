#include <stdio.h>

int main(void) {
    int seg_totais, horas, resto, minutos, segundos;
    scanf("%d", &seg_totais);

    horas = seg_totais / 3600;
    resto = seg_totais % 3600;
    minutos = resto / 60;
    segundos = resto % 60;

    printf("%d h %d m %d s\n", horas, minutos, segundos);
    return 0;
}
