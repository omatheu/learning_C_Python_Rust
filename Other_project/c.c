#include <stdio.h>

struct Vector {
    int x;
    int y;
    int z;
};

void incX(struct Vector *v); // Declaração da função com ponteiro

int main() {
    struct Vector v1 = {1, 2, 3};

    printf("Before: v1.x is equal to %d\n", v1.x);

    incX(&v1); // Passa o endereço de v1 para a função

    printf("After: v1.x is equal to %d\n", v1.x);

    return 0;
}

void incX(struct Vector *v) { // Usa ponteiro para a estrutura
    v->x++; // Acessa x através do ponteiro e incrementa
}
