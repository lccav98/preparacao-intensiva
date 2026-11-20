/* Exercicio A03-E05: Tabela com tabulacao e sequencias de escape */
#include <stdio.h>

int main(void) {
    printf("Comando\tFuncao\n");
    printf("\"gcc\"\tCompila C\n");
    printf("\\n\tNova linha\n");
    printf("\\\\\tBarra literal\n");
    return 0;
}
