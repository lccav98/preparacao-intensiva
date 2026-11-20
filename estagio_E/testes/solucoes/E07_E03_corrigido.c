#include <stdio.h>
#define ALTURA_MAX 500
#define LARGURA_MAX 500

int main(void) {
    static int img[ALTURA_MAX][LARGURA_MAX];
    int largura, altura, maxval, delta;

    scanf("%d %d %d", &largura, &altura, &maxval);
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
        }
    }

    printf("P2\n%d %d\n255\n", largura, altura);
    for (int i = 0; i < altura; i++) {
        for (int j = 0; j < largura; j++) {
            if (j > 0) {
                printf(" ");
            }
            printf("%d", img[i][j]);
        }
        printf("\n");
    }
    return 0;
}
