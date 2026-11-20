#include <stdio.h>

int contar_caractere(const char s[], int i, char c);
void imprimir_inversa(const char s[], int i);

int main(void) {
    char s[100], c;
    fgets(s, 100, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n' || s[i] == '\r') {
            s[i] = '\0';
            break;
        }
    }
    scanf(" %c", &c);

    printf("Ocorrencias: %d\n", contar_caractere(s, 0, c));
    printf("Inversa: ");
    imprimir_inversa(s, 0);
    printf("\n");
    return 0;
}

int contar_caractere(const char s[], int i, char c) {
    // Erro original 1: faltava o caso base para s[i] == '\0', lendo alem do fim da string.
    // Correcao: parar e retornar 0 ao encontrar o terminador '\0'.
    if (s[i] == '\0') {
        return 0;
    }
    // Erro original 2: passava i++ (pos-incremento), repetindo o mesmo indice i infinitamente.
    // Correcao: passar i + 1 para progredir ate '\0'.
    return (s[i] == c) + contar_caractere(s, i + 1, c);
}

void imprimir_inversa(const char s[], int i) {
    if (s[i] == '\0') {
        return;
    }
    // Erro original 3: imprimia s[i] antes da chamada recursiva (ordem direta).
    // Correcao: chamar recursivamente primeiro e imprimir s[i] no retorno (pos-recursao).
    imprimir_inversa(s, i + 1);
    printf("%c", s[i]);
}
