#include <stdio.h>
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

    int palavras = 0, letras_uteis = 0, em_palavra = 0;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] != ' ') {
            letras_uteis++;
            if (!em_palavra) {
                palavras++;
                em_palavra = 1;
            }
        } else {
            em_palavra = 0;
        }
        if (s[i] >= 'a' && s[i] <= 'z') {
            s[i] = (char)(s[i] - 'a' + 'A');
        }
    }

    double media = (palavras > 0) ? (double)letras_uteis / palavras : 0.0;
    printf("Maiuscula: %s\nMedia palavra: %.2f\n", s, media);
    return 0;
}
