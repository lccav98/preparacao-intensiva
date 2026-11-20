#include <stdio.h>

int aplicar_multa(int pontos, int infracao);

int main(void) {
    int pontos, infracao;
    scanf("%d %d", &pontos, &infracao);
    pontos = aplicar_multa(pontos, infracao);
    printf("Total de pontos: %d\n", pontos);
    return 0;
}

int aplicar_multa(int pontos, int infracao) {
    if (infracao > 0) {
        return pontos + infracao;
    }
    return pontos;
}
