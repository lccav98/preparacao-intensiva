#include <stdio.h>

void decompor_tempo(int total_seg, int *h, int *m, int *s);

int main(void) {
    int total_seg, h, m, s;
    scanf("%d", &total_seg);
    decompor_tempo(total_seg, &h, &m, &s);
    printf("%d h, %d min, %d s\n", h, m, s);
    return 0;
}

void decompor_tempo(int total_seg, int *h, int *m, int *s) {
    *h = total_seg / 3600;
    *m = (total_seg % 3600) / 60;
    *s = total_seg % 60;
}
