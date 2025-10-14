import streamlit as st
from views import View
import time

class AbriragendaUI:
    def main():
        st.header("Abrir Minha Agenda")
        data_consulta = st.text_input("Informe a data no formato dd/mm/aaaa")
        horario_inicio = st.text_input("Informe o horário inicial no formato HH:MM")
        horario_final = st.text_input("Informe o horário final no formato HH:MM")
        intervalo_consulta = st.text_input("Informe o intervalo entre os horários (min)")
        if st.button("Abrir Agenda"):
            View.cliente_inserir(data_consulta, horario_inicio, horario_final, intervalo_consulta)
            st.success("Agenda aberta com sucesso")
            time.sleep(2)
            st.rerun()