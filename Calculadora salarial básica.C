#include <stdio.h>

// 1. Calcula o salario bruto: valor da hora * horas trabalhadas no mes
double calcular_salario_bruto(double valor_hora, double horas_trabalhadas) {
    return valor_hora * horas_trabalhadas;
}

// 2. Calcula o desconto de 9% sobre o salario bruto
double calcular_desconto(double salario_bruto) {
    return salario_bruto * 0.09;
}

// 3. Calcula o salario liquido subtraindo o desconto do salario bruto
double calcular_salario_liquido(double salario_bruto, double desconto) {
    return salario_bruto - desconto;
}

int main(void) {
    double valor_hora, horas_trabalhadas;

    printf("=== Calculo de Salario por Hora ===\n");

    printf("Digite o valor da hora de trabalho: ");
    fflush(stdout);
    scanf("%lf", &valor_hora);

    printf("Digite a quantidade de horas trabalhadas no mes: ");
    fflush(stdout);
    scanf("%lf", &horas_trabalhadas);

    double bruto = calcular_salario_bruto(valor_hora, horas_trabalhadas);
    double desconto = calcular_desconto(bruto);
    double liquido = calcular_salario_liquido(bruto, desconto);

    printf("\n--- Resumo do Pagamento ---\n");
    printf("Salario bruto:   R$ %.2f\n", bruto);
    printf("Desconto (9%%):   R$ %.2f\n", desconto);
    printf("Salario liquido: R$ %.2f\n", liquido);

    return 0;
}
