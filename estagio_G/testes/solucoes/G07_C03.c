#include <stdio.h>

void remover_espacos(char s[], int i, int j);
int comprimento(const char s[], int i);

int main(void) {
    char s[100];
    fgets(s, 100, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n' || s[i] == '\r') {
            s[i] = '\0';
            break;
        }
    }

    remover_espacos(s, 0, 0);
    printf("Sem espacos: %s\n", s);
    printf("Comprimento: %d\n", comprimento(s, 0));
    return 0;
}

void remover_espacos(char s[], int i, int j) {
    if (s[i] == '\0') {
        s[j] = '\0';
        return;
    }
    if (s[i] != ' ') {
        s[j] = s[i];
        remover_espacos(s, i + 1, j + 1);
    } else {
        remover_espacos(s, i + 1, j);
    }
}

int comprimento(const char s[], int i) {
    if (s[i] == '\0') {
        return 0;
    }
    return 1 + comprimento(s, i + 1);
}
