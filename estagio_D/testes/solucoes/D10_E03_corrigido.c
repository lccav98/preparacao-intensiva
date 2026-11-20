#include <stdio.h>
#include <string.h>
#define MAX 101

int main(void) {
    char orig[MAX], norm[MAX];

    fgets(orig, MAX, stdin);
    int len = (int)strlen(orig);
    if (len > 0 && orig[len - 1] == '\n') {
        orig[len - 1] = '\0';
    }

    int j = 0, em_palavra = 0;
    for (int i = 0; orig[i] != '\0'; i++) {
        if (orig[i] != ' ') {
            if (j > 0 && !em_palavra) {
                norm[j++] = ' ';
            }
            norm[j++] = orig[i];
            em_palavra = 1;
        } else {
            em_palavra = 0;
        }
    }
    norm[j] = '\0';

    if (strcmp(norm, "SAIR") == 0) {
        printf("Encerrando\n");
    } else {
        printf("[%s] (%d)\n", norm, (int)strlen(norm));
    }
    return 0;
}
