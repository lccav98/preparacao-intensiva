#include <stdio.h>
#define MAX 20

int main(void) {
    int N, A[MAX][MAX];
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    for (int j = 0; j < N; j++) {
        int soma = 0;
        for (int i = 0; i < N; i++) {
            soma += A[i][j];
        }
        printf("Coluna %d: %d\n", j, soma);
    }

    int maior = A[0][0], li = 0, co = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (A[i][j] > maior) {
                maior = A[i][j];
                li = i;
                co = j;
            }
        }
    }
    printf("Maior: %d em (%d, %d)\n", maior, li, co);

    int id = 1;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if ((i == j && A[i][j] != 1) || (i != j && A[i][j] != 0)) {
                id = 0;
                break;
            }
        }
        if (!id) {
            break;
        }
    }
    printf("Identidade: %s\n", id ? "Sim" : "Nao");
    return 0;
}
