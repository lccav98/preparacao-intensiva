#include <stdio.h>
#define MAX_DIM 200

int main(void) {
    static int img[MAX_DIM][MAX_DIM];
    static int T[MAX_DIM][MAX_DIM];
    int largura, altura, delta;

    scanf("%d %d", &largura, &altura);
    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            scanf("%d", &img[i][j]);
        }
    }
    scanf("%d", &delta);

    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            img[i][j] += delta;
            if (img[i][j] < 0) {
                img[i][j] = 0;
            } else if (img[i][j] > 255) {
                img[i][j] = 255;
            }
            T[j][i] = img[i][j];
        }
    }

    printf("P2\n%d %d\n255\n", altura, largura);
    for (int i = 0; i < largura; i++) {
        for (int j = 0; j < altura; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", T[i][j]);
        }
        printf("\n");
    }
    return 0;
}
