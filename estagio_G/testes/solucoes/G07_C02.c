#include <stdio.h>

int comprimento(const char s[], int i);
int eh_palindromo(const char s[], int i, int j);
void inverter(char s[], int i, int j);

int main(void) {
    char s[100];
    scanf("%99s", s);

    int len = comprimento(s, 0);
    if (eh_palindromo(s, 0, len - 1)) {
        printf("Palindromo: Sim\n");
    } else {
        printf("Palindromo: Nao\n");
    }
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
    inverter(s, i + 1, j - 1);
}
