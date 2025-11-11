import streamlit as st
import pandas as pd
import time
from views import View

class ManterAvaliacaoUI:

    def main():
        st.header("Gerenciamento de Avaliações")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterAvaliacaoUI.listar()
        with tab2: ManterAvaliacaoUI.inserir()
        with tab3: ManterAvaliacaoUI.atualizar()
        with tab4: ManterAvaliacaoUI.excluir()

    def listar():
        avaliacoes = View.avaliacao_listar()

        if len(avaliacoes) == 0:
            st.write("Nenhuma avaliação cadastrada.")
        else:
            list_dic = []
            for obj in avaliacoes:
                list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        id_cliente = st.text_input("ID do Cliente")
        id_profissional = st.text_input("ID do Profissional")
        id_servico = st.text_input("ID do Serviço")
        nota = st.number_input("Nota (1 a 5)", min_value=1, max_value=5, step=1)
        comentario = st.text_area("Comentário")

        if st.button("Inserir"):
            try:
                View.avaliacao_inserir(id_cliente, id_profissional, id_servico, nota, comentario)
                st.success("Avaliação inserida com sucesso!")
                time.sleep(2)
                st.rerun()
            except Exception as e:
                st.error(f"Erro ao inserir avaliação: {e}")

    def atualizar():
        avaliacoes = View.avaliacao_listar()
        if len(avaliacoes) == 0:
            st.write("Nenhuma avaliação cadastrada.")
        else:
            op = st.selectbox("Selecione a Avaliação", avaliacoes)
            id_cliente = st.text_input("ID Cliente", op.get_id_cliente())
            id_profissional = st.text_input("ID Profissional", op.get_id_profissional())
            id_servico = st.text_input("ID Serviço", op.get_id_servico())
            nota = st.number_input("Nova Nota", 1, 5, op.get_nota())
            comentario = st.text_area("Comentário", op.get_comentario())

            if st.button("Atualizar"):
                id = op.get_id()
                View.avaliacao_atualizar(id, id_cliente, id_profissional, id_servico, nota, comentario)
                st.success("Avaliação atualizada com sucesso!")
                time.sleep(2)
                st.rerun()

    def excluir():
        avaliacoes = View.avaliacao_listar()
        if len(avaliacoes) == 0:
            st.write("Nenhuma avaliação cadastrada.")
        else:
            op = st.selectbox("Selecione a Avaliação", avaliacoes)

            if st.button("Excluir"):
                id = op.get_id()
                View.avaliacao_excluir(id)
                st.success("Avaliação excluída com sucesso!")
                time.sleep(2)
                st.rerun()
