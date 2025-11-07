import json

class Avaliacao:
    def __init__(self, id, nota, comentario, id_cliente, id_profissional, id_servico):
        self.id = id
        self.nota = nota
        self.comentario = comentario
        self.id_cliente = id_cliente
        self.id_profissional = id_profissional
        self.id_servico = id_servico

avaliacoes = []

def salvar_dados():
    dados = [a.__dict__ for a in avaliacoes]
    with open("avaliacoes.json", "w") as f:
        json.dump(dados, f, indent=4)

def carregar_dados():
    global avaliacoes
    try:
        with open("avaliacoes.json", "r") as f:
            lista = json.load(f)
            avaliacoes = [Avaliacao(**d) for d in lista]
    except FileNotFoundError:
        avaliacoes = []

def criar_avaliacao():
    print("\n=== Registrar Avaliação ===")
    id = input("ID da Avaliação: ")
    id_cliente = input("ID do Cliente: ")
    id_profissional = input("ID do Profissional: ")
    id_servico = input("ID do Serviço: ")
    nota = float(input("Nota (0 a 5): "))
    comentario = input("Comentário: ")

    nova = Avaliacao(id, nota, comentario, id_cliente, id_profissional, id_servico)
    avaliacoes.append(nova)
    salvar_dados()
    print("✅ Avaliação salva com sucesso!\n")

def listar_avaliacoes():
    print("\n=== Lista de Avaliações ===")
    if not avaliacoes:
        print("Nenhuma avaliação registrada.\n")
    else:
        for a in avaliacoes:
            print(f"ID: {a.id} | Nota: {a.nota} | Cliente: {a.id_cliente} | Profissional: {a.id_profissional}")
            print(f"Comentário: {a.comentario}")
            print("-" * 40)
    print()

def media_profissional():
    id_profissional = input("Digite o ID do profissional: ")
    notas = [a.nota for a in avaliacoes if a.id_profissional == id_profissional]
    if notas:
        media = sum(notas) / len(notas)
        print(f"Média de notas do profissional {id_profissional}: {media:.2f}\n")
    else:
        print("Esse profissional ainda não foi avaliado.\n")

carregar_dados()

while True:
    print("=== Sistema de Avaliações ===")
    print("1 - Registrar Avaliação")
    print("2 - Listar Avaliações")
    print("3 - Ver Média de um Profissional")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        criar_avaliacao()
    elif opcao == "2":
        listar_avaliacoes()
    elif opcao == "3":
        media_profissional()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida!\n")
