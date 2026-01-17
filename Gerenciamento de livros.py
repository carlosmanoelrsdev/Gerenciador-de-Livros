#importar biblioteca para gráficos
import matplotlib.pyplot as plt

#Definir classe livro
class Livro:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

#lista de livros
livros_cadastrados = [] #lista vazia para armazenar livros cadastrados pelo usuário
livros_principais = [
    Livro("Dom Casmurro", "Machado de Assis", "Romance", 5),
    Livro("O Cortiço", "Aluísio Azevedo", "Naturalismo", 3),
    Livro("Capitães da Areia", "Jorge Amado", "Romance", 4),
    Livro("Memórias Póstumas de Brás Cubas", "Machado de Assis", "Romance Filosófico", 6),
    Livro("A Hora da Estrela", "Clarice Lispector", "Drama", 2),
    Livro("Vidas Secas", "Graciliano Ramos", "Romance Regionalista", 5),
    Livro("O Guarani", "José de Alencar", "Romance Histórico", 3)
] #lista com alguns livros principais já cadastrados

#função unir livros
def unir_livros():
    return livros_principais + livros_cadastrados #usado para unir as duas listas de livros

#funções para gerenciar livros
#função cadastrar livro
def cadastrar_livro(titulo, autor, genero, quantidade):
    novo_livro = Livro(titulo, autor, genero, quantidade) #cria um novo objeto livro
    livros_cadastrados.append(novo_livro) #adiciona o novo livro à lista de livros cadastrados
    print(f'O livro {titulo} foi cadastrado com sucesso!') #confirmação de cadastro

def adicionar_livro():
    while True: #loop para garantir que o usuário insira um número válido
        try: #tratamento de erro para entrada inválida
            quant_de_livros = int(input('Quantos livros deseja cadastrar? '))
            if quant_de_livros < 0: #verifica se o número é negativo
                print('número inválido! tente novamente.')
                continue
        except ValueError: #captura erro de valor inválido
            print('Valor inválido! tente novamente.')
            continue
        break
    for c in range(quant_de_livros): #loop para cadastrar o número de livros desejado
        print(f'Cadastro do {c + 1}º livro:')
        titulo = input('Título do livro: ').strip() #strip() remove espaços extras
        autor = input('Autor do livro: ').strip()
        genero = input('Gênero do livro: ').strip()
        while True: #loop para garantir que o usuário insira um número válido
            try: #tratamento de erro para entrada inválida
                quantidade = int(input('Quantidade de livros: '))
                if quantidade <= 0:
                    print('Quantidade inválida! deve ser maior que zero. tente novamente.')
                    continue
            except ValueError:
                print('Valor inválido! tente novamente.')
                continue
            break
        cadastrar_livro(titulo, autor, genero, quantidade) #chama a função para cadastrar o livro


#função para listar livros
def listar_livros():
    todos_livros = unir_livros()
    print('lista de livros cadastrados:')
    for d in todos_livros: #loop para listar todos os livros
        print(f'    Título: {d.titulo}, Autor: {d.autor}, Gênero: {d.genero}, Quantidade: {d.quantidade}') #formata a saída paramelhor visualização
    print('fim da lista de livros.\n')

#função buscar livro
def buscar_livro():
    todos_livros = unir_livros()
    buscar = str(input('Nome do título do livro que deseja buscar: ')).strip().lower() #strip() remove espaços extras e lower() para deixar em minúsculo
    encontrado = False #flag para verificar se o livro foi encontrado
    for d in todos_livros: #loop para buscar o livro
        if d.titulo.lower() == buscar: #compara o título do livro em minúsculo
            print(f'Livro encontrado: Título: {d.titulo}, Autor: {d.autor}, Gênero: {d.genero}, Quantidade: {d.quantidade}')
            encontrado = True
            break #sai do loop se o livro for encontrado
    if not encontrado: #se o livro não foi encontrado
        print('Livro não encontrado\n finalizando busca...')

#função para gerar gráfico
def grafico_livros():
    todos_livros = unir_livros()
    contagem = {} #dicionário para contar a quantidade de livros por gênero
    for livro in todos_livros: #loop para contar os livros por gênero
        genero = livro.genero #pega o gênero do livro
        contagem[genero] = contagem.get(genero, 0) + livro.quantidade #soma a quantidade de livros por gênero
    genero = list(contagem.keys()) #pega os gêneros únicos
    quantidade = list(contagem.values()) #pega as quantidades correspondentes
    #gerar gráfico
    plt.figure(figsize=(10, 6)) #define o tamanho da figura
    plt.bar(genero, quantidade) #cria o gráfico de barras
    plt.xlabel('Gênero') #nome do eixo x
    plt.ylabel('Quantidade de Livros') #nome do eixo y
    plt.title('Quantidade de Livros por Gênero') #título do gráfico
    plt.xticks(rotation=45) #rotaciona os rótulos do eixo x para melhor visualização
    plt.tight_layout() #ajusta o layout para evitar cortes
    plt.show() #exibe o gráfico

#função principal para executar o programa
def main():
    print(f'{"-="*15} Bem-vindo ao Sistema de Gerenciamento de Livros! {"-="*15}')
    while True:
        print("\nEscolha uma opção:")
        print("1 - Cadastrar livros")
        print("2 - Listar livros")
        print("3 - Buscar livro")
        print("4 - Ver gráfico de livros por gênero")
        print("0 - Sair")
        escolha = input("Opção: ").strip()
        if escolha == "1":
            adicionar_livro()
        elif escolha == "2":
            listar_livros()
        elif escolha == "3":
            buscar_livro()
        elif escolha == "4":
            grafico_livros()
        elif escolha == "0":
            print("Obrigado por usar o sistema! Finalizando...")
            break
        else:
            print("Opção inválida. Tente novamente.")
    
#executar a função principal
main()


