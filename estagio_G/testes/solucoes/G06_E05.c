#include <stdio.h>

int comprimento(const char s[], int i);
int iguais(const char a[], const char b[], int i);

int main(void) {
    char a[50], b[50];
    scanf("%49s %49s", a, b);

    printf("Comp A: %d\n", comprimento(a, 0));
    printf("Comp B: %d\n", comprimento(b, 0));
    if (iguais(a, b, 0)) {
        printf("Iguais: Sim\n");
    } else {
        printf("Iguais: Nao\n");
    }
    return 0;
}

int comprimento(const char s[], int i) {
    if (s[i] == '\0') {
        return 0;
    }
    return 1 + comprimento(s, i + 1);
}

int iguais(const char a[], const char b[], int i) {
    if (a[i] != b[i]) {
        return 0;
    }
    if (a[i] == '\0') {
        return 1;
    }
    return iguais(a, b, i + 1);
}
