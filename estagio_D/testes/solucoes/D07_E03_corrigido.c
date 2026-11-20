#include <stdio.h>
#define MAX 101

int main(void) {
    char orig[MAX];
    char dest[MAX];

    fgets(orig, MAX, stdin);
    for (int i = 0; orig[i] != '\0'; i++) {
        if (orig[i] == '\n') {
            orig[i] = '\0';
            break;
        }
    }

    int palavras = 0;
    int em_palavra = 0;
    int j = 0;

    for (int i = 0; orig[i] != '\0'; i++) {
        if (orig[i] != ' ') {
            if (!em_palavra) {
                palavras++;
                em_palavra = 1;
            }
        } else {
            em_palavra = 0;
        }

        if (!(orig[i] >= '0' && orig[i] <= '9')) {
            dest[j] = orig[i];
            j++;
        }
    }
    dest[j] = '\0';

    printf("Palavras: %d\nLimpa: [%s]\n", palavras, dest);
    return 0;
}
