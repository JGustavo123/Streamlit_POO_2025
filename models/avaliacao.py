import json

class Avaliacao:
    def __init__(self, id, id_cliente, id_profissional, id_servico, nota, comentario):
        self.__id = id
        self.__id_cliente = id_cliente
        self.__id_profissional = id_profissional
        self.__id_servico = id_servico
        self.__nota = nota
        self.__comentario = comentario

    def get_id(self): return self.__id
    def get_id_cliente(self): return self.__id_cliente
    def get_id_profissional(self): return self.__id_profissional
    def get_id_servico(self): return self.__id_servico
    def get_nota(self): return self.__nota
    def get_comentario(self): return self.__comentario

    def set_id(self, id): self.__id = id
    def set_id_cliente(self, id_cliente): self.__id_cliente = id_cliente
    def set_id_profissional(self, id_profissional): self.__id_profissional = id_profissional
    def set_id_servico(self, id_servico): self.__id_servico = id_servico
    def set_nota(self, nota): self.__nota = nota
    def set_comentario(self, comentario): self.__comentario = comentario

    def to_json(self):
        return {
            "id": self.__id,
            "id_cliente": self.__id_cliente,
            "id_profissional": self.__id_profissional,
            "id_servico": self.__id_servico,
            "nota": self.__nota,
            "comentario": self.__comentario
        }

    @staticmethod
    def from_json(dic):
        return Avaliacao(dic["id"], dic["id_cliente"], dic["id_profissional"], dic["id_servico"], dic["nota"], dic["comentario"])

    def __str__(self):
        return f"{self.__id} - Cliente {self.__id_cliente} - Profissional {self.__id_profissional} - Nota {self.__nota}"


class AvaliacaoDAO:
    __objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.__objetos:
            if aux.get_id() > id:
                id = aux.get_id()
        obj.set_id(id + 1)
        cls.__objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__objetos

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        for i, aux in enumerate(cls.__objetos):
            if aux.get_id() == obj.get_id():
                cls.__objetos[i] = obj
                cls.salvar()
                return

    @classmethod
    def excluir(cls, id):
        cls.abrir()
        cls.__objetos = [obj for obj in cls.__objetos if obj.get_id() != id]
        cls.salvar()

    @classmethod
    def abrir(cls):
        cls.__objetos = []
        try:
            with open("avaliacoes.json", "r", encoding="utf-8") as arquivo:
                lista = json.load(arquivo)
                for dic in lista:
                    cls.__objetos.append(Avaliacao.from_json(dic))
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("avaliacoes.json", "w", encoding="utf-8") as arquivo:
            json.dump(cls.__objetos, arquivo, default=lambda obj: obj.to_json(), ensure_ascii=False, indent=4)
