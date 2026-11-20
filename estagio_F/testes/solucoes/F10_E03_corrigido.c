#include <stdio.h>

void resumo(const int v[], int n, int *soma, int *maior);
void limpar_espacos(char s[]);

int main(void) {
    char s[100];
    int n, v[50], soma, maior;

    fgets(s, 100, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n' || s[i] == '\r') {
            s[i] = '\0';
            break;
        }
    }

    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &v[i]);
    }

    // Erro original 1: passava soma (int) em vez de &soma (int *).
    // Correcao: passar o endereco &soma por valor.
    resumo(v, n, &soma, &maior);
    limpar_espacos(s);

    printf("Soma: %d\n", soma);
    printf("Maior: %d\n", maior);
    printf("Sem espacos: %s\n", s);
    return 0;
}

void resumo(const int v[], int n, int *soma, int *maior) {
    // Erro original 2: fazia soma = 0; (anulando a copia local do ponteiro) em vez de *soma = 0;.
    // Correcao: desreferenciar *soma para inicializar a variavel de main.
    *soma = 0;
    *maior = v[0];
    for (int i = 0; i < n; i++) {
        *soma += v[i];
        if (v[i] > *maior) {
            *maior = v[i];
        }
    }
}

void limpar_espacos(char s[]) {
    int j = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] != ' ') {
            s[j] = s[i];
            j++;
        }
    }
    // Erro original 3: nao gravava '\0' ao final da string modificada in-place.
    // Correcao: encerrar a string com s[j] = '\0';.
    s[j] = '\0';
}
