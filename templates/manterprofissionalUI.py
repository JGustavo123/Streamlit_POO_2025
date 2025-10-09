import streamlit as st
import pandas as pd
from views import View
import time

class manterprofissionalUI:
    def main():
        st.header("Cadastro de Profissionais")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: manterprofissionalUI.listar()
        with tab2: manterprofissionalUI.inserir()
        with tab3: manterprofissionalUI.atualizar()
        with tab4: manterprofissionalUI.excluir()

    def listar():
        profissional = View.profissional_listar()
        if len(profissional) == 0: st.write("Nenhum profissional cadastrado")
        else:
            list_dic = []
            for obj in profissional: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        especialidade = st.text_input("Informe a especialidade ")
        conselho = st.text_input("Informe o conselho")
        if st.button("Inserir"):
            View.profissional_inserir(nome, email, senha, especialidade, conselho)
            st.success("Profissional inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        profissional = View.profissional_listar()
        if len(profissional) == 0: st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Atualização de profissional", profissional)
            nome = st.text_input("Informe o novo nome", op.get_nome())
            especialidade = st.text_input("Informe a nova especialidade", op.get_especialidade())
            conselho = st.text_input("Informe o novo conselho", op.get_conselho())
            if st.button("Atualizar"):
                id = op.get_id()
                View.profissional_atualizar(id, nome, especialidade, conselho)
                st.success("profissional atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        profissional = View.profissional_listar()
        if len(profissional) == 0: st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Exclusão de profissional", profissional)
            if st.button("Excluir"):
                id = op.get_id()
                View.profissional_excluir(id)
                st.success("Profissional excluído com sucesso")
                time.sleep(2)
                st.rerun()