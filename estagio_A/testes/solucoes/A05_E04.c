/* Exercicio A05-E04: Exibicao de constantes #define e const sem expressoes */
#include <stdio.h>
#define PI 3.14159

int main(void) {
    const int ESCALA = 2;
    double raio = 4.5;
    char unidade = 'm';

    printf("PI aproximado: %.4f\n", PI);
    printf("Escala: %i\n", ESCALA);
    printf("Raio: %.2f %c\n", raio, unidade);
    return 0;
}
