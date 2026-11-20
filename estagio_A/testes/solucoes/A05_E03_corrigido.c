/* Exercicio A05-E03: Correcao de #define e especificadores */
#include <stdio.h>
#define LIMITE 100

int main(void) {
    double peso = 72.453;
    char classe = 'A';

    printf("Limite: %d | Peso: %.2f kg | Classe: %c\n", LIMITE, peso, classe);
    return 0;
}
