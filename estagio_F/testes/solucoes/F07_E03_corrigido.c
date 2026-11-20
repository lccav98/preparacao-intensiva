#include <stdio.h>

#define COL 3

int somar_matriz(const int m[][COL], int linhas);
void remover_digitos(char s[]);

int main(void) {
    int linhas, m[10][COL];
    char texto[50];

    scanf("%d", &linhas);
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < COL; j++) {
            scanf("%d", &m[i][j]);
        }
    }
    scanf("%49s", texto);

    printf("Soma: %d\n", somar_matriz(m, linhas));
    remover_digitos(texto);
    printf("Texto: %s\n", texto);
    return 0;
}

// Erro original 1: omitia o numero de colunas (const int m[][]), o que impede o compilador de calcular o deslocamento das linhas.
// Correcao: informar obrigatoriamente a dimensao das colunas (const int m[][COL]).
int somar_matriz(const int m[][COL], int linhas) {
    int soma = 0;
    for (int i = 0; i < linhas; i++) {
        for (int j = 0; j < COL; j++) {
            soma += m[i][j];
        }
    }
    return soma;
}

void remover_digitos(char s[]) {
    int j = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] < '0' || s[i] > '9') {
            s[j] = s[i];
            j++;
        }
    }
    // Erro original 2: nao inseria o terminador '\0' na nova posicao final j.
    // Correcao: encerrar explicitamente a string modificada com s[j] = '\0';.
    s[j] = '\0';
}
