#include <stdio.h>

int contar_vogais(const char s[], int i);
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

    printf("Vogais: %d\n", contar_vogais(s, 0));
    printf("Inversa: ");
    imprimir_inversa(s, 0);
    printf("\n");
    return 0;
}

int contar_vogais(const char s[], int i) {
    if (s[i] == '\0') {
        return 0;
    }
    char c = s[i];
    int eh_vogal = (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
                    c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U');
    return eh_vogal + contar_vogais(s, i + 1);
}

void imprimir_inversa(const char s[], int i) {
    if (s[i] == '\0') {
        return;
    }
    imprimir_inversa(s, i + 1);
    printf("%c", s[i]);
}
