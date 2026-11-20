#include <stdio.h>
#define MAX 101

int main(void) {
    char orig[MAX];
    char norm[MAX];

    fgets(orig, MAX, stdin);
    for (int i = 0; orig[i] != '\0'; i++) {
        if (orig[i] == '\n') {
            orig[i] = '\0';
            break;
        }
    }

    int j = 0;
    int em_palavra = 0;
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

    printf("[%s]\n", norm);
    return 0;
}
