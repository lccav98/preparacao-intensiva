#include <stdio.h>

int comprimento(const char s[], int i);
int eh_palindromo(const char s[], int i, int j);
void inverter(char s[], int i, int j);

int main(void) {
    char s[100];
    fgets(s, 100, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n' || s[i] == '\r') {
            s[i] = '\0';
            break;
        }
    }

    int len = comprimento(s, 0);
    if (eh_palindromo(s, 0, len - 1)) {
        printf("Palindromo: Sim\n");
    } else {
        printf("Palindromo: Nao\n");
    }

    // Erro original 3: passava len em vez de len - 1, trocando '\0' com s[0].
    // Correcao: passar o indice do ultimo caractere valido (len - 1).
    inverter(s, 0, len - 1);
    printf("Invertida: %s\n", s);
    return 0;
}

int comprimento(const char s[], int i) {
    if (s[i] == '\0') {
        return 0;
    }
    return 1 + comprimento(s, i + 1);
}

int eh_palindromo(const char s[], int i, int j) {
    // Erro original 1: usava i == j, falhando em strings de tamanho par ou vazias.
    // Correcao: usar i >= j para cobrir tamanhos pares, impares e string vazia.
    if (i >= j) {
        return 1;
    }
    if (s[i] != s[j]) {
        return 0;
    }
    return eh_palindromo(s, i + 1, j - 1);
}

void inverter(char s[], int i, int j) {
    if (i >= j) {
        return;
    }
    char aux = s[i];
    s[i] = s[j];
    s[j] = aux;
    // Erro original 2: mantinha j fixo na chamada recursiva em vez de j - 1.
    // Correcao: convergir ambos os indices com i + 1 e j - 1.
    inverter(s, i + 1, j - 1);
}
