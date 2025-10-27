import json

class Cliente:
    def __init__(self, id, nome, email, fone, senha):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_senha(senha)

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def get_senha(self): return self.__senha

    def set_id(self, id):
        try: 
            if id is None or id == "": raise ValueError("ID não pode estar vazio")
            self.__id = id
        except Exception as Erro: raise ValueError(Erro)

    def set_nome(self, nome): 
        try: 
            if nome is None or nome == "": raise ValueError("Nome não pode estar vazio")
            self.__nome = nome
        except Exception as Erro: raise ValueError(Erro)

    def set_email(self, email):
        try: 
            if email is None or email == "": raise ValueError("E-mail não pode estar vazio")
            else: self.__email = email
        except Exception as Erro: raise ValueError(Erro)

    def set_fone(self, fone): 
        try: 
            if fone is None or fone == "": raise ValueError("Fone não pode estar vazio")
            self.__fone = fone
        except Exception as Erro: raise ValueError(Erro)

    def set_senha(self, senha): 
        try: 
            if senha is None or senha == "": raise ValueError("Senha não pode estar vazio")
            self.__senha = senha
        except Exception as Erro: raise ValueError(Erro)

    def to_json(self):
        dic = {"id":self.__id, "nome":self.__nome, "email":self.__email, "fone":self.__fone, "senha":self.__senha}
        return dic

    
    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"], dic["senha"])

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}, - {self.__senha}"

class ClienteDAO:
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
            with open("clientes.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Cliente.from_json(dic)
                    cls.__objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default = Cliente.to_json)  
