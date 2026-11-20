#include <stdio.h>
#include "texto.h"

int main(void) {
    char s[100], ch;
    fgets(s, 100, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n' || s[i] == '\r') {
            s[i] = '\0';
            break;
        }
    }
    scanf(" %c", &ch);
    printf("Ocorrencias: %d\n", contar_ocorrencias(s, ch));
    para_maiusculas(s);
    printf("Maiusculas: %s\n", s);
    return 0;
}
