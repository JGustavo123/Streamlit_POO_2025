import streamlit as st
from models.manteravaliacao import Avaliacao

class ManterAvaliacaoUI:
    @staticmethod
    def main():
        st.title("📋 Gerenciar Avaliações")

        menu = st.radio("Escolha uma opção:", ["Registrar", "Listar", "Média por Profissional"])

        if menu == "Registrar":
            ManterAvaliacaoUI.registrar()
        elif menu == "Listar":
            ManterAvaliacaoUI.listar()
        elif menu == "Média por Profissional":
            ManterAvaliacaoUI.media_profissional()

    @staticmethod
    def registrar():
        st.subheader("Registrar Avaliação")
        id = st.text_input("ID da Avaliação")
        id_cliente = st.text_input("ID do Cliente")
        id_profissional = st.text_input("ID do Profissional")
        id_servico = st.text_input("ID do Serviço")
        nota = st.slider("Nota", 0.0, 5.0, 3.0, 0.5)
        comentario = st.text_area("Comentário")

        if st.button("Salvar Avaliação"):
            if id and id_cliente and id_profissional and id_servico:
                a = Avaliacao(id, nota, comentario, id_cliente, id_profissional, id_servico)
                a.salvar()
                st.success("✅ Avaliação salva com sucesso!")
            else:
                st.warning("Preencha todos os campos obrigatórios.")

    @staticmethod
    def listar():
        st.subheader("Lista de Avaliações")
        lista = Avaliacao.listar()
        if not lista:
            st.info("Nenhuma avaliação cadastrada.")
        else:
            for a in lista:
                st.write(f"**ID:** {a.id}")
                st.write(f"**Nota:** {a.nota}")
                st.write(f"**Cliente:** {a.id_cliente}")
                st.write(f"**Profissional:** {a.id_profissional}")
                st.write(f"**Comentário:** {a.comentario}")
                st.write("---")

    @staticmethod
    def media_profissional():
        st.subheader("Média de Avaliações por Profissional")
        id_profissional = st.text_input("ID do Profissional")
        if st.button("Calcular Média"):
            media = Avaliacao.media_profissional(id_profissional)
            if media is not None:
                st.success(f"Média de notas do profissional {id_profissional}: {media:.2f}")
            else:
                st.info("Esse profissional ainda não foi avaliado.")
