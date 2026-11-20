#include <stdio.h>

void remover_caractere(char s[], char c);

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
    remover_caractere(s, c);
    printf("Resultado: %s\n", s);
    return 0;
}

void remover_caractere(char s[], char c) {
    int j = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] != c) {
            s[j] = s[i];
            j++;
        }
    }
    s[j] = '\0';
}
