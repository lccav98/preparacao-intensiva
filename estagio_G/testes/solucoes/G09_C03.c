#include <stdio.h>

void remover_vogais(char s[], int i, int j);
void imprimir_inversa(const char s[], int i);

int main(void) {
    char s[100];
    fgets(s, 100, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n' || s[i] == '\r') {
            s[i] = '\0';
            break;
        }
    }

    remover_vogais(s, 0, 0);
    printf("Sem vogais: %s\n", s);
    printf("Inversa: ");
    imprimir_inversa(s, 0);
    printf("\n");
    return 0;
}

void remover_vogais(char s[], int i, int j) {
    if (s[i] == '\0') {
        s[j] = '\0';
        return;
    }
    char c = s[i];
    int vogal = (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
                 c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U');
    if (!vogal) {
        s[j] = s[i];
        remover_vogais(s, i + 1, j + 1);
    } else {
        remover_vogais(s, i + 1, j);
    }
}

void imprimir_inversa(const char s[], int i) {
    if (s[i] == '\0') {
        return;
    }
    imprimir_inversa(s, i + 1);
    printf("%c", s[i]);
}
