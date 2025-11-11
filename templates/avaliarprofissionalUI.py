import streamlit as st
import time
from views import View

class AvaliarProfissionalUI:
    def main():
        st.header("Avaliar Profissional")

        profissionais = View.profissional_listar()
        if len(profissionais) == 0:
            st.write("Nenhum profissional cadastrado.")
            return

        profissional = st.selectbox("Selecione o profissional que atendeu você:", profissionais)
        nota = st.slider("Dê uma nota de 1 a 5:", 1, 5, 3)
        comentario = st.text_area("Deixe um comentário sobre o atendimento:")

        if st.button("Enviar Avaliação"):
            try:
                id_cliente = st.session_state["usuario_id"]
                id_profissional = profissional.get_id()
                View.avaliacao_inserir(id_cliente, id_profissional, nota, comentario)
                st.success("Avaliação enviada com sucesso!")
                time.sleep(2)
                st.rerun()
            except Exception as e:
                st.error(f"Erro ao enviar avaliação: {e}")
