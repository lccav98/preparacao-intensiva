#include <stdio.h>

int contar_acima(const int v[], int n, int limite);

int main(void) {
    int n, lim, v[50];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }
    scanf("%d", &lim);
    // Erro original 1: passava n + 1, lendo posicao invalida v[n] fora dos limites.
    // Correcao: passar exatamente n.
    printf("Acima: %d\n", contar_acima(v, n, lim));
    return 0;
}

int contar_acima(const int v[], int n, int limite) {
    int cont = 0;
    for (int i = 0; i < n; i++) {
        if (v[i] > limite) {
            cont++;
        }
        // Erro original 2: tentava executar v[i] = 0; dentro de parametro const int v[].
        // Correcao: remover a escrita em v[i], preservando o contrato de somente leitura.
    }
    return cont;
}
