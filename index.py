import streamlit as st
from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterServicoUI
from templates.manterhorarioUI import ManterHorarioUI
from templates.manterprofissionalUI import ManterProfissionalUI
from templates.abrircontaUI import AbrirContaUI
from templates.agendarservicoUI import AgendarServicoUI
from templates.loginUI import LoginUI
from templates.perfilclienteUI import PerfilClienteUI
from templates.perfilprofissionalUI import PerfilProfissionalUI
from templates.abriragendaUI import AbrirAgendaUI
from templates.visualizaragendaUI import VisualizarAgendaUI
from templates.visualizarservicosUI import VisualizarServicosUI
from templates.confirmarservicoUI import ConfirmarServicoUI
from templates.alterarsenhaUI import AlterarSenhaUI
from templates.manteravaliacaoUI import ManterAvaliacaoUI
from views import View


class IndexUI:

    def menu_admin():            
        op = st.sidebar.selectbox(
            "Menu", 
            [
                "Cadastro de Clientes",
                "Cadastro de Serviços",
                "Cadastro de Horários",
                "Cadastro de Profissionais",
                "Alterar Senha"
            ]
        )

        if op == "Cadastro de Clientes": ManterClienteUI.main()
        elif op == "Cadastro de Serviços": ManterServicoUI.main()
        elif op == "Cadastro de Horários": ManterHorarioUI.main()
        elif op == "Cadastro de Profissionais": ManterProfissionalUI.main()
        elif op == "Alterar Senha": AlterarSenhaUI.main()

    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        elif op == "Abrir Conta": AbrirContaUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Agendar Serviço", "Visualizar Serviços"])
        if op == "Meus Dados": PerfilClienteUI.main()
        elif op == "Agendar Serviço": AgendarServicoUI.main()
        elif op == "Visualizar Serviços": VisualizarServicosUI.main()
            
    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Abrir Minha Agenda", "Visualizar Agenda", "Confirmar Serviço", "Ver Avaliações"])
        if op == "Meus Dados": PerfilProfissionalUI.main()
        elif op == "Abrir Minha Agenda": AbrirAgendaUI.main()
        elif op == "Visualizar Agenda": VisualizarAgendaUI.main()
        elif op == "Confirmar Serviço": ConfirmarServicoUI.main()
        elif op == "Ver Avaliações": ManterAvaliacaoUI.main()

    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
            admin = st.session_state["usuario_nome"] == "admin"
            tipo = st.session_state.get("tipo_usuario", "")

            if admin:
                IndexUI.menu_admin()
            elif tipo == "profissional":
                IndexUI.menu_profissional()
            else:
                IndexUI.menu_cliente()

            IndexUI.sair_do_sistema()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            for chave in ["usuario_id", "usuario_nome", "tipo_usuario"]:
                if chave in st.session_state:
                    del st.session_state[chave]
            st.rerun()

    def main():
        st.set_page_config(page_title="Sistema", layout="wide")
        View.cliente_criar_admin()
        IndexUI.sidebar()

IndexUI.main()
