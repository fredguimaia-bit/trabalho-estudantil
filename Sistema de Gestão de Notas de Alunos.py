# Sistema de Gestão de Notas de Alunos
import os

def ler_nota(mensagem):
    """Garante que o usuário digite um número válido entre 0 e 10."""
    while True:
        try:
            valor = float(input(mensagem))
            if 0 <= valor <= 10:
                return valor
            print("[-] Atenção: A nota deve estar entre 0 e 10.")
        except ValueError:
            print("[-] Erro: Digite apenas números válidos (ex: 7.5).")

def calcular_situacao(media):
    """Define a situação acadêmica baseada na média."""
    if media >= 7.0:
        return "Aprovado(a) direto! 🎉"
    elif 4.0 <= media < 7.0:
        return "em Recuperação ⚠️"
    else:
        return "Reprovado(a) ❌"

def gerar_relatorio(nome, notas, media, situacao):
    """Gera o texto do relatório e o salva em um arquivo de texto."""
    conteudo = f"""
---------------------------------------
           RELATÓRIO FINAL             
---------------------------------------
Aluno(a): {nome}
Notas: {notas[0]}, {notas[1]}, {notas[2]}, {notas[3]}
Média Final: {media:.1f}
Situação: {situacao}
---------------------------------------
"""
    print(conteudo)
    
    # Salva automaticamente em um arquivo .txt
    nome_arquivo = f"relatorio_{nome.lower().replace(' ', '_')}.txt"
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo.strip())
    print(f"[+] Relatório salvo com sucesso no arquivo: '{nome_arquivo}'\n")

# --- FLUXO PRINCIPAL ---
if __name__ == "__main__":
    print("=== SISTEMA DE GESTÃO DE NOTAS ===")
    nome = input("Digite seu nome: ")
    print(f"Olá, {nome}, bem-vindo(a)!\n")

    # Coletando notas com validação
    notas = []
    for i in range(1, 5):
        nota = ler_nota(f"Digite a nota {i} (0 a 10): ")
        notas.append(nota)

    # Calculando média
    media = sum(notas) / len(notas)
    situacao = calcular_situacao(media)

    # Exibindo e salvando o relatório
    gerar_relatorio(nome, notas, media, situacao)
