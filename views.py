from models.cliente import Cliente, ClienteDAO
from models.servico import servico, ServicoDAO
from models.horario import Horario, HorarioDAO
from models.profissional import profissional, profissionalDAO

class View:

    def cliente_criar_admin():
        for c in View.cliente_listar():
            if c.get_email() == "admin": 
                return 
        View.cliente_inserir("admin", "admin", "fone", "1234")

    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
               return {"id": c.get_id(), "nome": c.get_nome()}
        return None

    def cliente_listar():
        return ClienteDAO.listar()
    
    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)
    
    def cliente_inserir(nome, email, fone, senha):
        cliente_obj = Cliente(0, nome, email, fone, senha)
        ClienteDAO.inserir(cliente_obj)
    

    def cliente_atualizar(id, nome, email, fone, senha):
        cliente_obj = Cliente(id, nome, email, fone, senha)
        ClienteDAO.atualizar(cliente_obj)
    
    def cliente_excluir(id):
        cliente_obj = Cliente(id, "", "", "")
        ClienteDAO.excluir(cliente_obj)
    

    def servico_listar():
        return ServicoDAO.listar()
    
    def servico_listar_id(id):
        return ServicoDAO.listar_id(id)
    
    def servico_inserir(descricao, valor):
        servico_obj = servico(0, descricao, valor)  # variável renomeada
        ServicoDAO.inserir(servico_obj)
    
    def servico_atualizar(id, descricao, valor):
        servico_obj = servico(id, descricao, valor)  # variável renomeada
        ServicoDAO.atualizar(servico_obj)
    
    def servico_excluir(id):
        servico_obj = servico(id, "", 0)  # variável renomeada
        ServicoDAO.excluir(servico_obj)


    def horario_inserir(data, confirmado, id_cliente, id_servico):
        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        HorarioDAO.inserir(c)

    def horario_listar():
        return HorarioDAO.listar()
    
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico):
        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        HorarioDAO.atualizar(c)

    def horario_excluir(id):
        c = Horario(id, None)
        HorarioDAO.excluir(c)

    
    def profissional_listar():
        return profissionalDAO.listar()
    
    def profissional_listar_id(id):
        return profissionalDAO.listar_id(id)
    
    def profissional_inserir(nome, especialidade, conselho):
        profissional_obj = profissional(0, nome, especialidade, conselho)
        profissionalDAO.inserir(profissional_obj)
    
    def profissional_atualizar(id, nome, especialidade, conselho):
        profissional_obj = profissional(id, nome, especialidade, conselho)
        profissionalDAO.atualizar(profissional_obj)
    
    def profissional_excluir(id):
        profissional_obj = profissional(id, "", "", "")
        profissionalDAO.excluir(profissional_obj)