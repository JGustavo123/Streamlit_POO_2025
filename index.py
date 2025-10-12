from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import manterservicoUI
from templates.manterhorarioUI import ManterHorarioUI
from templates.manterprofissionalUI import manterprofissionalUI
from templates.abrircontaUI import abrircontaUI
from templates.loginUI import loginUI
from templates.perfilUI import PerfilUI

from views import View
import streamlit as st

class IndexUI:

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
    
    def profissional_autenticar(email, senha):
        for p in View.profissional_listar():
            if p.get_email() == email and p.get_senha() == senha:
                return {"id": p.get_id(), "nome": p.get_nome()}
        return None

    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": loginUI.main()
        if op == "Abrir Conta": abrircontaUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados"])
        if op == "Meus Dados": PerfilUI.main()
    
    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Meus Dados"])
        if op == "Meus Dados": PerfilUI.main()
    
    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Horários", "Cadastro de profissionais"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": manterservicoUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        if op == "Cadastro de profissionais": manterprofissionalUI.main()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()

    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()

        else:
            admin = st.session_state["usuario_nome"] == "admin"
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
            if admin: IndexUI.menu_admin()
            else: IndexUI.menu_cliente()
            IndexUI.sair_do_sistema()

    def main():
        # verifica a existe o usuário admin
        View.cliente_criar_admin()
        # monta o sidebar
        IndexUI.sidebar()

    
IndexUI.main()