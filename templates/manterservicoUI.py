import streamlit as st
import pandas as pd
from views import View
import time

class manterservicoUI:
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: manterservicoUI.listar()
        with tab2: manterservicoUI.inserir()
        with tab3: manterservicoUI.atualizar()
        with tab4: manterservicoUI.excluir()

    def listar():
        servico = View.servico_listar()
        if len(servico) == 0: st.write("nenhum serviço no momento")
        else:
            list_dic = []
            for obj in servico: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        descricao = st.text_input("Informe a descrição")
        valor = st.text_input("Informe o valor")
        if st.button("Inserir"):
            View.servico_inserir(descricao, valor)
            st.success("Serviço inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        servico = View.servico_listar()
        if len(servico) == 0: st.write("Nenhum serviço cadastrado")
        else:
            op = st.selectbox("Atualização de serviço", servico)
            descricao = st.text_input("Informe a descricao", op.get_descricao())
            valor = st.text_input("Informe o novo valor", op.get_valor())
            if st.button("Atualizar"):
                id = op.get_id()
                View.servico_atualizar(id, descricao, valor)
                st.success("Serviço atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        servico = View.servico_listar()
        if len(servico) == 0: st.write("Nenhum serviço cadastrado")
        else:
            op = st.selectbox("Exclusão de serviço", servico)
            if st.button("Excluir"):
                id = op.get_id()
                View.servico_excluir(id)
                st.success("Serviço excluído com sucesso")
                time.sleep(2)
                st.rerun()