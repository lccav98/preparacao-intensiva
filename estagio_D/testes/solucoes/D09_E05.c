#include <stdio.h>
#define MAX_GRADE 101
#define MAX_LINHA 11
#define INDICE(i, j, cols) ((i) * (cols) + (j))

int main(void) {
    int l, c, q;
    char grade[MAX_GRADE];
    char buf[MAX_LINHA];

    scanf("%d %d", &l, &c);
    for (int i = 0; i < l; i++) {
        scanf("%10s", buf);
        for (int j = 0; j < c; j++) {
            grade[INDICE(i, j, c)] = buf[j];
        }
    }
    grade[l * c] = '\0';

    scanf("%d", &q);
    for (int k = 0; k < q; k++) {
        int r, s;
        scanf("%d %d", &r, &s);
        if (r >= 0 && r < l && s >= 0 && s < c) {
            printf("%c\n", grade[INDICE(r, s, c)]);
        } else {
            printf("Invalido\n");
        }
    }

    printf("Linear: %s\n", grade);
    return 0;
}
