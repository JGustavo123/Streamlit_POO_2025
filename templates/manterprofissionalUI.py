import streamlit as st
import pandas as pd
from views import View
import time

class ManterProfissionalUI:
    
    def main():
        st.header("Cadastro de Profissionis")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProfissionalUI.listar()
        with tab2: ManterProfissionalUI.inserir()
        with tab3: ManterProfissionalUI.atualizar()
        with tab4: ManterProfissionalUI.excluir()

    def listar():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else:
            list_dic = []
            for obj in profissionais: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Nome")
        email = st.text_input("E-mail")
        senha = st.text_input("Senha", type="password")
        especialidade = st.text_input("Especialidade")
        conselho = st.text_input("Conselho")

        if st.button("Inserir"):
            try:
                View.profissional_inserir(nome, email, senha, especialidade, conselho )
                st.success("Profissional inserido com sucesso!")
                time.sleep(2)
                st.rerun()
            except Exception as e:
                st.error(f"Erro ao inserir profissional: {e}")

    def atualizar():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Atualização de Profissionais", profissionais)
            nome = st.text_input("Informe o novo nome", op.get_nome())
            email = st.text_input("Informe o novo email", op.get_email())
            senha = st.text_input("Informe a nova senha", op.get_senha())
            especialidade = st.text_input("Informe a nova especialidade", op.get_especialidade())
            conselho = st.text_input("Informe o novo conselho", op.get_conselho())

            if st.button("Atualizar"):
                try:    
                    id = op.get_id()
                    View.profissional_atualizar(id, nome, email, senha, especialidade, conselho)
                    st.success("Profissional atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao atualizar profissional: {e}")

    def excluir():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Exclusão de Profissionals", profissionais)

            if st.button("Excluir"):
                try:
                    id = op.get_id()
                    View.profissional_excluir(id)
                    st.success("Profissional excluído com sucesso")
                    time.sleep(2)
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao excluir profissional: {e}")