#include "texto_ops.h"

int contar_letras(const char s[]) {
    int cont = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if ((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <= 'Z')) {
            cont++;
        }
    }
    return cont;
}

void substituir_caractere(char s[], char antigo, char novo) {
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == antigo) {
            s[i] = novo;
        }
    }
}
