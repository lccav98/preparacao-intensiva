#include <stdio.h>
#define MAX 101

int main(void) {
    int k, ch;
    char s[MAX];

    scanf("%d", &k);
    while ((ch = getchar()) != '\n' && ch != EOF) {
    }

    fgets(s, MAX, stdin);
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n') {
            s[i] = '\0';
            break;
        }
    }

    int shift = ((k % 26) + 26) % 26;
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] >= 'A' && s[i] <= 'Z') {
            s[i] = (char)('A' + (s[i] - 'A' + shift) % 26);
        } else if (s[i] >= 'a' && s[i] <= 'z') {
            s[i] = (char)('a' + (s[i] - 'a' + shift) % 26);
        }
    }

    printf("Cifrada: %s\n", s);
    return 0;
}
