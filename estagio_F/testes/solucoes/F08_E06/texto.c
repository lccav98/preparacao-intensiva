#include "texto.h"

int contar_ocorrencias(const char s[], char ch) {
    int cont = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == ch) {
            cont++;
        }
    }
    return cont;
}

void para_maiusculas(char s[]) {
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] >= 'a' && s[i] <= 'z') {
            s[i] = (char)(s[i] - 'a' + 'A');
        }
    }
}
