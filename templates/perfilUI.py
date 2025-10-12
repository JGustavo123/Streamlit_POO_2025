import streamlit as st
from views import View
import time

class PerfilUI:
    def main():
        st.header("Meus Dados")

        tipo = st.session_state.get("usuario_tipo", "cliente")
        usuario_id = st.session_state.get("usuario_id")

        if usuario_id is None:
            st.error("Usuario não autenticado.")
            return

        if tipo == "cliente":
            op = View.cliente_listar_id(usuario_id)
        else:
            op = View.profissional_listar_id(usuario_id)
            
        if op is None:
            st.error("Erro: usuário não encontrado.")
            return

        nome = st.text_input("Nome", op.get_nome())
        email = st.text_input("E-mail", op.get_email())
        senha = st.text_input("Senha", op.get_senha(), type="password")

        if tipo == "cliente":
            fone = st.text_input("Fone", op.get_fone())
        else:
            conselho = st.text_input("Conselho", op.get_conselho())
            especialidade = st.text_input("Especialidade", op.get_especialidade())
    
        if st.button("Atualizar"):
            id = op.get_id()

            if tipo == "cliente":
                View.cliente_atualizar(id, nome, email, fone, senha)
            else:
                View.profissional_atualizar(id, nome, email, senha, especialidade, conselho)

            
            st.success(f"{tipo} atualizado com sucesso")
            time.sleep(1)
            st.rerun()