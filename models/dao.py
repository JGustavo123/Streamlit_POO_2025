import json
from typing import Type, List

class DAO:
    _arquivo: str = None
    _model: Type = None
    _objetos: List = []

    @classmethod
    def _serialize_list(cls, lista):
        out = []
        for obj in lista:
            if hasattr(obj, "to_json"):
                out.append(obj.to_json())
            elif hasattr(obj, "to_dict"):
                out.append(obj.to_dict())
            else:
                raise AttributeError
        return out
    
    @classmethod
    def _deserialize_list(cls, list_dic):
        out = []
        for dic in list_dic:
            if hasattr(cls._model, "from.json"):
                out.append(cls._model.from_json(dic))
            elif hasattr(cls._model, "from_dict"):
                out.append(cls._model.from_dict(dic))
            else:
                raise AttributeError
        return out
    
    @classmethod
    def abrir(cls):
        cls._objetos = []
        if cls._arquivo is None or cls._model is None:
            raise RuntimeError
        try:
            with open(cls.arquivo, "r", encoding="utf-8") as f:
                list_dic = json.load(f)
                cls._objetos = cls._deserialize_list(list_dic)
        except FileNotFoundError:
            cls._objetos = []
        except json.JSONDecodeError:
            cls._objetos = []

    @classmethod
    def salvar(cls):
        if cls._arquivo is None or cls._model is None:
            raise RuntimeError
        with open(cls._arquivo, "w", encoding="utf-8") as f:
            json.dump(cls._serialize_list(cls._objetos), f, indent=4, ensure_ascii=False)

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls._objetos
    
    @classmethod
    def listar_id(cls, id_):
        cls.abrir()
        for obj in cls._objetos:
            if hasattr(obj, "get_id") and obj.get_id() == id_:
                return obj
        return None
    
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        max_id = max([o.get_id() for o in cls._objetos], default=0)
        if hasattr(obj, "set_id"):
            obj.set_id(max_id + 1)
        else:
            try:
                obj._id = max_id + 1
            except:
                pass
        cls._objetos.append(obj)
        cls.salvar
    
    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        for i, o in enumerate(cls._objetos):
            if o.get_id() == obj.get_id():
                cls._objetos[i] = obj
                cls.salvar()
                return
        cls._objetos.append(obj)
        cls.salvar()

    @classmethod
    def excluir(cls,obj):
        cls.abrir()
        cls._objetos = [o for o in cls._objetos if o.get_id() != obj.get_id()]
        cls.salvar()