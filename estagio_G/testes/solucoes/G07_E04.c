#include <stdio.h>

int comprimento(const char s[], int i);
int eh_palindromo(const char s[], int i, int j);

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
    return 0;
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
