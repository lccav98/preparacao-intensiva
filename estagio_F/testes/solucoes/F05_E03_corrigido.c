#include <stdio.h>

void trocar(int *a, int *b);

int main(void) {
    int x, y;
    scanf("%d %d", &x, &y);
    trocar(&x, &y);
    printf("%d %d\n", x, y);
    return 0;
}

void trocar(int *a, int *b) {
    // Erro original: int *aux; declarava ponteiro nao inicializado (endereco indefinido),
    // causando comportamento indefinido ao tentar gravar em *aux = *a.
    // Correcao: aux deve armazenar um valor inteiro comum (int), nao um endereco.
    int aux = *a;
    *a = *b;
    *b = aux;
}
