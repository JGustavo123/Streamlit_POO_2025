from models.cliente import Cliente, ClienteDAO
from models.servico import servico, ServicoDAO
from models.horario import Horario, HorarioDAO

class View:

    def cliente_listar():
        return ClienteDAO.listar()
    
    def cliente_inserir(nome, email, fone):
        cliente_obj = Cliente(0, nome, email, fone)
        ClienteDAO.inserir(cliente_obj)
    
    def cliente_atualizar(id, nome, email, fone):
        cliente_obj = Cliente(id, nome, email, fone)
        ClienteDAO.atualizar(cliente_obj)
    
    def cliente_excluir(id):
        cliente_obj = Cliente(id, "", "", "")
        ClienteDAO.excluir(cliente_obj)
    

    def servico_listar():
        return ServicoDAO.listar()
    
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