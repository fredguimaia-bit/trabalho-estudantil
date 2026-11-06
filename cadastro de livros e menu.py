#estrutura do livro
class Livro:
    def __init__(self, titulo,autor,genero,quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

    def __str__(self):
        return f"'{self.titulo}' - {self.autor} [{self.genero}] (Disponíveis: {self.quantidade})"

#Biblioteca de Livros
biblioteca = [
    Livro("Dom Casmurro", "Machado de Assis", "Romance", 5),
    Livro("O Hobbit", "J.R.R. Tolkien", "Fantasia", 3),
    Livro("1984", "George Orwell", "Ficção", 2),
    Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia", 4),
    Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", "Fantasia", 6),
    Livro("A Culpa é das Estrelas", "John Green", "Romance", 1),
    Livro("O Alquimista", "Paulo Coelho", "Ficção", 3),
    Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "Infantil", 2)
]
#passo 3: cadastrar, procurar e listar
def cadastrar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    genero = input("Digite o gênero do livro: ")
    quantidade = int(input("Digite a quantidade disponível: "))

    novo_livro = Livro(titulo, autor, genero, quantidade)
    biblioteca.append(novo_livro)
    print("Livro cadastrado com sucesso!")

def listar_livros():
    if len(biblioteca) == 0:
        print("Nenhum livro cadastrado na biblioteca.\n")
    else:
        print("--- LISTA DE LIVROS ---")
        for livro in biblioteca:
            print("Título:", livro.titulo)
            print("Autor:", livro.autor)
            print("Gênero:", livro.genero)
            print("Quantidade:", livro.quantidade)

def buscar_Livro():
    titulo_busca = input("Digite o título do livro que deseja buscar: ")
    encontrado = False

    for Livro in biblioteca:
        if Livro.titulo.lower() == titulo_busca.lower():
            print("\n--- LIVRO ENCONTRADO ---")
            print("Título:", Livro.titulo)
            print("Autor:", Livro.autor)
            print("Gênero:", Livro.genero)
            print("Quantidade:", Livro.quantidade)
            encontrado = True
            break
    if not encontrado:
        print("Livro não encontrado.\n")

#Passo 4:Utilizar a biblioteca Matplotlib para gerar um gráfico

import matplotlib.pyplot as plt
def gerar_grafico_generos():
    if len(biblioteca) == 0:
        return
    generos = {}
    for livro in biblioteca:
        if livro.genero in generos:
            generos[livro.genero] += 1
        else:
            generos[livro.genero] = 1
    generos = list(generos.items())
    quantidade = [quantidade for genero, quantidade in generos]
    generos = [genero for genero, quantidade in generos]
    plt.bar(generos, quantidade)
    plt.xlabel("Gênero")
    plt.ylabel("Quantidade")
    plt.title("Quantidade de Livros por Gênero")
    plt.show()

def menu():
    while True:
        print("\n=== SISTEMA DE BIBLIOTECA ===")
        print("1. Cadastrar Livro")
        print("2. Listar Livros")
        print("3. Buscar Livro por Título")
        print("4. Gerar Gráfico de Gêneros")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            buscar_Livro()
        elif opcao == "4":
            gerar_grafico_generos()
        elif opcao == "0":
            print("Encerrando o sistema de biblioteca. Até logo!")
            break
        else:
            print("Opção inválida! Por favor, tente novamente.")

# Executar o menu
menu()
