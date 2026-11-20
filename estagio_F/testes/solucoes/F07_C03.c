#include <stdio.h>

void remover_vogais(char s[]);
int tamanho_string(const char s[]);

int main(void) {
    char s[100];
    fgets(s, 100, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n' || s[i] == '\r') {
            s[i] = '\0';
            break;
        }
    }
    remover_vogais(s);
    printf("Sem vogais: %s\n", s);
    printf("Comprimento: %d\n", tamanho_string(s));
    return 0;
}

void remover_vogais(char s[]) {
    int j = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        char c = s[i];
        int vogal = (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
                     c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U');
        if (!vogal) {
            s[j] = s[i];
            j++;
        }
    }
    s[j] = '\0';
}

int tamanho_string(const char s[]) {
    int len = 0;
    while (s[len] != '\0') {
        len++;
    }
    return len;
}
