#include <stdio.h>

void remover_caractere(char s[], int i, int j, char c);

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

    remover_caractere(s, 0, 0, c);
    printf("Resultado: %s\n", s);
    return 0;
}

void remover_caractere(char s[], int i, int j, char c) {
    if (s[i] == '\0') {
        s[j] = '\0';
        return;
    }
    if (s[i] != c) {
        s[j] = s[i];
        remover_caractere(s, i + 1, j + 1, c);
    } else {
        remover_caractere(s, i + 1, j, c);
    }
}
