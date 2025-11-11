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
        if not avaliacoes:
            st.write("Nenhuma avaliação cadastrada.")
        else:
            list_dic = [obj.to_json() for obj in avaliacoes]
            df = pd.DataFrame(list_dic)
            st.dataframe(df, use_container_width=True)

    def inserir():
        st.subheader("Inserir Avaliação")
        id_cliente = st.text_input("ID do Cliente")
        id_profissional = st.text_input("ID do Profissional")
        id_servico = st.text_input("ID do Serviço")
        nota = st.number_input("Nota (1 a 5)", min_value=1, max_value=5, step=1)
        comentario = st.text_area("Comentário")

        if st.button("Inserir Avaliação"):
            try:
                View.avaliacao_inserir(id_cliente, id_profissional, id_servico, nota, comentario)
                st.success("✅ Avaliação inserida com sucesso!")
                time.sleep(1.5)
                st.rerun()
            except Exception as e:
                st.error(f"Erro ao inserir avaliação: {e}")

    def atualizar():
        st.subheader("Atualizar Avaliação")
        avaliacoes = View.avaliacao_listar()
        if not avaliacoes:
            st.write("Nenhuma avaliação cadastrada.")
        else:
            op = st.selectbox("Selecione a Avaliação", avaliacoes, format_func=lambda a: f"ID {a.get_id()} - Cliente {a.get_id_cliente()}")
            id_cliente = st.text_input("ID Cliente", op.get_id_cliente())
            id_profissional = st.text_input("ID Profissional", op.get_id_profissional())
            id_servico = st.text_input("ID Serviço", op.get_id_servico())
            nota = st.number_input("Nova Nota", 1, 5, op.get_nota())
            comentario = st.text_area("Comentário", op.get_comentario())

            if st.button("Atualizar Avaliação"):
                try:
                    id = op.get_id()
                    View.avaliacao_atualizar(id, id_cliente, id_profissional, id_servico, nota, comentario)
                    st.success("✅ Avaliação atualizada com sucesso!")
                    time.sleep(1.5)
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao atualizar avaliação: {e}")

    def excluir():
        st.subheader("Excluir Avaliação")
        avaliacoes = View.avaliacao_listar()
        if not avaliacoes:
            st.write("Nenhuma avaliação cadastrada.")
        else:
            op = st.selectbox("Selecione a Avaliação", avaliacoes, format_func=lambda a: f"ID {a.get_id()} - Cliente {a.get_id_cliente()}")
            if st.button("Excluir Avaliação"):
                try:
                    id = op.get_id()
                    View.avaliacao_excluir(id)
                    st.success("🗑️ Avaliação excluída com sucesso!")
                    time.sleep(1.5)
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao excluir avaliação: {e}")

    def avaliar():
        st.header("⭐ Avaliar Profissional")

        id_cliente = st.session_state.get("usuario_id")
        if not id_cliente:
            st.warning("⚠️ Você precisa estar logado como cliente para avaliar.")
            return

        profissionais = View.profissional_listar()
        if not profissionais:
            st.write("Nenhum profissional cadastrado.")
            return

        prof_op = st.selectbox(
            "Selecione o profissional:",
            profissionais,
            format_func=lambda p: f"{p.get_nome()} (ID {p.get_id()})"
        )
        id_profissional = prof_op.get_id()

        servicos = View.servico_listar()
        if not servicos:
            st.write("Nenhum serviço cadastrado.")
            return

        serv_op = st.selectbox(
            "Selecione o serviço:",
            servicos,
            format_func=lambda s: f"{s.get_descricao()} (ID {s.get_id()})"
        )
        id_servico = serv_op.get_id()

        nota = st.slider("Nota (1 a 5)", 1, 5, 5)
        comentario = st.text_area("Comentário (opcional)")

        if st.button("Enviar Avaliação"):
            try:
                View.avaliacao_inserir(id_cliente, id_profissional, id_servico, nota, comentario)
                st.success("✅ Avaliação enviada com sucesso!")
                time.sleep(1.5)
                st.rerun()
            except Exception as e:
                st.error(f"Erro ao enviar avaliação: {e}")
