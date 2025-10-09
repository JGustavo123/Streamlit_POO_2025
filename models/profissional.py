import json

class profissional:
    def __init__(self, id, nome, email, senha, especialidade, conselho):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_senha(senha)
        self.set_especialidade(especialidade)
        self.set_conselho(conselho)


    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_senha(self): return self.__senha
    def get_especialidade(self): return self.__especialidade
    def get_conselho(self): return self.__conselho

    def set_id(self, id): self.__id = id
    def set_nome(self, nome): self.__nome = nome
    def set_email(self, email): self.__email = email
    def set_senha(self, senha): self.__senha = senha
    def set_especialidade(self, especialidade): self.__especialidade = especialidade
    def set_conselho(self, conselho): self.__conselho = conselho

    def to_json(self):
        dic = {"id":self.__id, "nome":self.__nome, "email":self.__email, "senha":self.__senha, "especialidade":self.__especialidade, "conselho":self.__conselho}
        return dic
    
    @staticmethod
    def from_json(dic):
        return profissional(dic["id"], dic["nome"], dic["email"], dic["senha"], dic["especialidade"], dic["conselho"])

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__senha} - {self.__especialidade} - {self.__conselho}"

class profissionalDAO:
    __objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.__objetos:
            if aux.get_id() > id: id = aux.get_id()
        obj.set_id(id + 1)
        cls.__objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.__objetos: 
            if obj.get_id() == id: return obj
        return None

    @classmethod
    def atualizar(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.__objetos.remove(aux)
            cls.__objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.__objetos.remove(aux)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.__objetos = []
        try:
            with open("profissional.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = profissional.from_json(dic)
                    cls.__objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("profissional.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default = profissional.to_json)