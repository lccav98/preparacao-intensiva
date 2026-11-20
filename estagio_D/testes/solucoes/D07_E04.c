#include <stdio.h>
#include <ctype.h>
#define MAX 101

int main(void) {
    char s[MAX];

    fgets(s, MAX, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n') {
            s[i] = '\0';
            break;
        }
    }

    int comp = 0, vogais = 0, digitos = 0, palavras = 0;
    int em_palavra = 0;

    for (int i = 0; s[i] != '\0'; i++) {
        char c = (char)tolower((unsigned char)s[i]);
        comp++;
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            vogais++;
        }
        if (isdigit((unsigned char)s[i])) {
            digitos++;
        }
        if (s[i] != ' ') {
            if (!em_palavra) {
                palavras++;
                em_palavra = 1;
            }
        } else {
            em_palavra = 0;
        }
    }

    printf("Comprimento: %d\nVogais: %d\nDigitos: %d\nPalavras: %d\n",
           comp, vogais, digitos, palavras);
    return 0;
}
