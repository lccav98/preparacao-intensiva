#ifndef FUNCOES_H
#define FUNCOES_H

#include "imagem.h"

void ordenar(int v[], int n);
void aplicarMediana(int img[ALTURA][LARGURA]);
void copiarImagem(const int orig[ALTURA][LARGURA], int dest[ALTURA][LARGURA]);
int contarAlterados(const int a[ALTURA][LARGURA], const int b[ALTURA][LARGURA]);

#endif
