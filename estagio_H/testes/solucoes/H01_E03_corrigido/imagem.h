#ifndef IMAGEM_H
#define IMAGEM_H
// Correcao: adicionadas guardas #ifndef/#define/#endif contra inclusao dupla

#define ALTURA 3
#define LARGURA 4

int lerImagem(int img[ALTURA][LARGURA]);
void salvarImagem(const int img[ALTURA][LARGURA]);

#endif
