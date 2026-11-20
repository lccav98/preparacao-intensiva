#include <stdio.h>

void imprimir_linha(int n, char ch) {
    for (int i = 0; i < n; i++) {
        printf("%c", ch);
    }
    printf("\n");
}

int fatorial(int n) {
    int fat = 1;
    for (int i = 2; i <= n; i++) {
        fat *= i;
    }
    return fat;
}

int main(void) {
    int n;
    char ch;
    scanf("%d %c", &n, &ch);
    imprimir_linha(n, ch);
    printf("Fatorial: %d\n", fatorial(n));
    return 0;
}
