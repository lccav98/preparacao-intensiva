#include <stdio.h>
#include "texto_ops.h"

int main(void) {
    char s[100], antigo, novo;
    fgets(s, 100, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n' || s[i] == '\r') {
            s[i] = '\0';
            break;
        }
    }
    scanf(" %c %c", &antigo, &novo);
    substituir_caractere(s, antigo, novo);
    printf("Texto: %s\n", s);
    printf("Letras: %d\n", contar_letras(s));
    return 0;
}
