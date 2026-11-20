#include <stdio.h>

void remover_char(char s[], int i, int j, char c);
int comprimento(const char s[], int i);
int eh_palindromo(const char s[], int i, int j);

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

    remover_char(s, 0, 0, c);
    int len = comprimento(s, 0);

    printf("Limpa: %s\n", s);
    printf("Comprimento: %d\n", len);
    if (eh_palindromo(s, 0, len - 1)) {
        printf("Palindromo: Sim\n");
    } else {
        printf("Palindromo: Nao\n");
    }
    return 0;
}

void remover_char(char s[], int i, int j, char c) {
    if (s[i] == '\0') {
        s[j] = '\0';
        return;
    }
    if (s[i] != c) {
        s[j] = s[i];
        remover_char(s, i + 1, j + 1, c);
    } else {
        remover_char(s, i + 1, j, c);
    }
}

int comprimento(const char s[], int i) {
    if (s[i] == '\0') {
        return 0;
    }
    return 1 + comprimento(s, i + 1);
}

int eh_palindromo(const char s[], int i, int j) {
    if (i >= j) {
        return 1;
    }
    if (s[i] != s[j]) {
        return 0;
    }
    return eh_palindromo(s, i + 1, j - 1);
}
