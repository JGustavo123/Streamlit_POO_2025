import json

class Avaliacao:
    ARQUIVO = "avaliacoes.json"

    def __init__(self, id, nota, comentario, id_cliente, id_profissional, id_servico):
        self.id = id
        self.nota = nota
        self.comentario = comentario
        self.id_cliente = id_cliente
        self.id_profissional = id_profissional
        self.id_servico = id_servico

    @staticmethod
    def listar():
        try:
            with open(Avaliacao.ARQUIVO, "r") as f:
                lista = json.load(f)
                return [Avaliacao(**d) for d in lista]
        except FileNotFoundError:
            return []

    def salvar(self):
        avaliacoes = Avaliacao.listar()
        avaliacoes.append(self)
        dados = [a.__dict__ for a in avaliacoes]
        with open(Avaliacao.ARQUIVO, "w") as f:
            json.dump(dados, f, indent=4)

    @staticmethod
    def media_profissional(id_profissional):
        lista = Avaliacao.listar()
        notas = [a.nota for a in lista if a.id_profissional == id_profissional]
        if notas:
            return sum(notas) / len(notas)
        return None

