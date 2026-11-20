#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define MAX 41

int main(void) {
    char s1[MAX], s2[MAX], aux[MAX];

    scanf("%40s %40s", s1, s2);

    if (strcmp(s1, s2) > 0) {
        strcpy(aux, s1);
        strcpy(s1, s2);
        strcpy(s2, aux);
    }

    int len = (int)strlen(s1);
    int i = 0, j = len - 1, eh_pal = 1;
    while (i < j) {
        if (tolower((unsigned char)s1[i]) != tolower((unsigned char)s1[j])) {
            eh_pal = 0;
            break;
        }
        i++;
        j--;
    }

    printf("Ordem: %s <= %s\nPalindromo menor: %s\n",
           s1, s2, eh_pal ? "Sim" : "Nao");
    return 0;
}
