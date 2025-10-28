from models.cliente import Cliente, ClienteDAO
from models.servico import Servico, ServicoDAO
from models.horario import Horario, HorarioDAO
from models.profissional import Profissional, ProfissionalDAO
from datetime import datetime

class View:

    def cliente_criar_admin():
        for c in View.cliente_listar():
            if c.get_email() == "admin": return
        View.cliente_inserir("admin", "admin", "fone", "1234")
    
    def cliente_listar():
        r = ClienteDAO.listar()
        r.sort(key = lambda obj : obj.get_nome())
        return r
    
    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)
    
    def cliente_inserir(nome, email, fone, senha):
        exist = True
        missing = False
        for c in View.cliente_listar():
            if c.get_email().lower() == email.lower():
                exist = True
                raise ValueError("Já existe um cliente com esse email")
            else: exist = False
            if nome() == "" or email == "" or fone == "" or senha == "":
                missing = True
                raise ValueError("Falta informação no cliente")
            else: missing = False
        if (exist==False) and (missing==False):
            cliente = Cliente(0, nome, email, fone, senha)
            ClienteDAO.inserir(cliente)

    def cliente_atualizar(id, nome, email, fone, senha):
        cliente = Cliente(id, nome, email, fone, senha)
        ClienteDAO.atualizar(cliente)

    def cliente_excluir(id):
        for h in View.horario_listar():
            if h.get_id_cliente() == id:
                raise ValueError("Não é possível excluir um cliente que já possui agendamentos.")


    def servico_listar():
        r = ServicoDAO.listar()
        r.sort(key = lambda obj : obj.get_descricao())
        return r
    
    def servico_listar_id(id):
        return ServicoDAO.listar_id(id)
    
    def servico_inserir(id, descricao, valor):
        servico = Servico(id, descricao, valor)
        ServicoDAO.inserir(servico)

    def servico_atualizar(id, descricao, valor):
        servico = Servico(id, descricao, valor)
        ServicoDAO.atualizar(servico)

    def servico_excluir(id):
        servico = Servico(id, "", 0)
        ServicoDAO.excluir(servico)


    def horario_agendar_horario(id_profissional):
        r = []
        agora = datetime.now()
        for h in View.horario_listar():
            if h.get_data() >= agora and h.get_confirmado() == False and h.get_id_cliente() == None and h.get_id_profissional() == id_profissional:
                r.append(h)
        r.sort(key= lambda h : h.get_data())
        return r   
         
    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)
        HorarioDAO.inserir(c)

    def horario_listar():
        r = HorarioDAO.listar()
        r.sort(key = lambda obj : obj.get_data())
        return r
    
    @staticmethod
    def horario_listar_id(id):
        horarios = View.horario_listar()
        for h in horarios:
            if h.get_id() == id:
                return h
        return None

    def horario_filtrar_profissional(id_profissional):
        r = []
        for h in View.horario_listar():
            if h.get_id_profissional() == id_profissional:
                r.append(h)
        return r
    
    def horario_filtrar_cliente(id_cliente):
        r = []
        for h in View.horario_listar():
            if h.get_id_profissional() == id_cliente:
                r.append(h)
        return r
    
    def horario_atualizar_obj(horario):
        HorarioDAO.atualizar(horario)

    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
        h = Horario(id, data)
        h.set_confirmado(confirmado)
        h.set_id_cliente(id_cliente)
        h.set_id_servico(id_servico)
        h.set_id_profissional(id_profissional)
        HorarioDAO.atualizar(h)

    def horario_excluir(id):
        c = Horario(id, None)
        HorarioDAO.excluir(c)


    def profissional_inserir(nome, especialidade, conselho, email, senha):

        exist = True
        missing = False
        for pro in View.profissional_listar():
            if pro.get_email().lower() == email.lower():
                exist = True
                raise ValueError("já existe um profissional com esse e-mail")
            else: exist = False
        for c in View.cliente_listar():
            if c.get_email().lower() == email.lower():
                exist = True
                raise ValueError("Já existe um cliente com esse e-mail")
            else: exist = False
            if nome == "" or email == "" or senha == "":
                missing = True
                raise ValueError("Falta informação no profissional")
            else: missing = False
        if (exist==False) and (missing==False):
            profissional = Profissional(0, nome, especialidade, conselho, email, senha)
            ProfissionalDAO.inserir(profissional)

    def profissional_atualizar(id, nome, especialidade, conselho, email, senha):

        exist = True
        missing = False
        for pro in View.profissional_listar():
            if pro.get_email().lower() == email.lower() and pro.get_id() != id:
                exist = True
                raise ValueError("Já existe um profissional com esse e-mail")
            else: exist = False
        for c in View.cliente_listar():
            if c.get_email().lower() == email.lower():
                exist = True
                raise ValueError("Já existe um cliente com esse e-mail")
            else: exist = False
            if nome == "" or email == "" or senha == "":
                missing = True
                raise ValueError("Falta informação no cliente")
            else: missing = False
        if (exist==False) and (missing==False):
            profissional = Profissional(id, nome, especialidade, conselho, email, senha)
            ProfissionalDAO.atualizar(profissional)

    def profissional_excluir(id):
        for h in View.horario_listar():
            if h.get_id_profissional() == id:
                raise ValueError("Não é possível excluir um profissional que já criou uma agenda.")

    def profissional_excluir(id):
        p = Profissional(id, "0", "0", "0", "0", "0")
        ProfissionalDAO.excluir(p)

    def profissional_listar():
        r = ProfissionalDAO.listar()
        r.sort(key = lambda obj : obj.get_nome())
        return r

    def profissional_listar_id(id):
        return ProfissionalDAO.listar_id(id)

    def profissional_autenticar(email, senha):
        for p in ProfissionalDAO.listar():
            if p.get_email() == email and p.get_senha() == senha:
                return {"id": p.get_id(), "nome": p.get_nome()}
        return None
