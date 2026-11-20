#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define MAX_PAL 31

int main(void) {
    int n;
    char atual[MAX_PAL];
    char menor[MAX_PAL], maior[MAX_PAL];
    int palindromos = 0;

    scanf("%d", &n);
    for (int k = 0; k < n; k++) {
        scanf("%30s", atual);
        if (k == 0) {
            strcpy(menor, atual);
            strcpy(maior, atual);
        } else {
            if (strcmp(atual, menor) < 0) {
                strcpy(menor, atual);
            }
            if (strcmp(atual, maior) > 0) {
                strcpy(maior, atual);
            }
        }

        int len = (int)strlen(atual);
        int i = 0, j = len - 1, eh_pal = 1;
        while (i < j) {
            if (tolower((unsigned char)atual[i]) != tolower((unsigned char)atual[j])) {
                eh_pal = 0;
                break;
            }
            i++;
            j--;
        }
        if (eh_pal) {
            palindromos++;
        }
    }

    printf("Menor: %s\nMaior: %s\nPalindromos: %d\n", menor, maior, palindromos);
    return 0;
}
