#include <stdio.h>

int main(void) {
    int vendas[5];
    int soma = 0;

    printf("=== Registro de Vendas Diarias (5 dias) ===\n");

    // 1. Leitura dos 5 valores e armazenamento no vetor
    for (int i = 0; i < 5; i++) {
        printf("Digite a quantidade de vendas do dia %d: ", i + 1);
        fflush(stdout);
        scanf("%d", &vendas[i]);
    }

    // 2. Calculo da soma dos elementos do vetor
    for (int i = 0; i < 5; i++) {
        soma += vendas[i];
    }

    // 3. Exibicao de cada elemento (um por linha) e da soma total
    printf("\n--- Vendas por dia ---\n");
    for (int i = 0; i < 5; i++) {
        printf("Dia %d: %d\n", i + 1, vendas[i]);
    }

    printf("\nTotal geral de vendas no periodo: %d\n", soma);

    return 0;
}
