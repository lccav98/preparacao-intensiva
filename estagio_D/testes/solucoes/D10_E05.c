#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define MAX 101

int main(void) {
    char orig[MAX], norm[MAX];
    int vog[5] = {0};

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

            char c = (char)tolower((unsigned char)orig[i]);
            if (c == 'a') {
                vog[0]++;
            } else if (c == 'e') {
                vog[1]++;
            } else if (c == 'i') {
                vog[2]++;
            } else if (c == 'o') {
                vog[3]++;
            } else if (c == 'u') {
                vog[4]++;
            }
        } else {
            em_palavra = 0;
        }
    }
    norm[j] = '\0';

    printf("[%s]\na:%d e:%d i:%d o:%d u:%d\n",
           norm, vog[0], vog[1], vog[2], vog[3], vog[4]);
    return 0;
}
