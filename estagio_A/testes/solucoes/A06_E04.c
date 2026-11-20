#include <stdio.h>

int main(void) {
    int id_a, id_b;
    double min_val, max_val;

    scanf("%d %d", &id_a, &id_b);
    scanf("%lf %lf", &min_val, &max_val);

    printf("IDs: %d e %d\n", id_a, id_b);
    printf("Limites: %.2f a %.2f\n", min_val, max_val);
    return 0;
}
