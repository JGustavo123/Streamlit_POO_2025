from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import manterservicoUI
from templates.manterhorarioUI import ManterHorarioUI
from templates.manterprofissionalUI import manterprofissionalUI
import streamlit as st

class IndexUI:

    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Horários", "Cadastro de profissionais"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": manterservicoUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        if op == "Cadastro de Profissionais": manterprofissionalUI.main()
    def sidebar():
        IndexUI.menu_admin()
    def main():
        IndexUI.sidebar()

IndexUI.main()