#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define MAX 101

int main(void) {
    char s[MAX];

    fgets(s, MAX, stdin);
    int len = (int)strlen(s);
    if (len > 0 && s[len - 1] == '\n') {
        s[len - 1] = '\0';
        len--;
    }

    int i = 0;
    int j = len - 1;
    int eh_pal = 1;

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

    if (eh_pal) {
        printf("Palindromo\n");
    } else {
        printf("Nao palindromo\n");
    }
    return 0;
}
