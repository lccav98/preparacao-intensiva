#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define MAX 101

int main(void) {
    char s[MAX];
    int freq[26] = {0};

    fgets(s, MAX, stdin);
    int len = (int)strlen(s);
    if (len > 0 && s[len - 1] == '\n') {
        s[len - 1] = '\0';
        len--;
    }

    int i = 0, j = len - 1, eh_pal = 1;
    while (i < j) {
        while (i < j && s[i] == ' ') {
            i++;
        }
        while (i < j && s[j] == ' ') {
            j--;
        }
        if (tolower((unsigned char)s[i]) != tolower((unsigned char)s[j])) {
            eh_pal = 0;
            break;
        }
        i++;
        j--;
    }

    int tem_letra = 0;
    for (int k = 0; k < len; k++) {
        char c = (char)tolower((unsigned char)s[k]);
        if (c >= 'a' && c <= 'z') {
            freq[c - 'a']++;
            tem_letra = 1;
        }
    }

    printf("Palindromo: %s\n", eh_pal ? "Sim" : "Nao");
    if (!tem_letra) {
        printf("Sem letras\n");
    } else {
        for (int k = 0; k < 26; k++) {
            if (freq[k] > 0) {
                printf("%c: %d\n", 'a' + k, freq[k]);
            }
        }
    }
    return 0;
}
