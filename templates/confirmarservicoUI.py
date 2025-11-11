import streamlit as st
from views import View

class ConfirmarServicoUI:

    @staticmethod
    def main():
        # --- Mostrar mensagem de sucesso logo no início ---
        if "msg" in st.session_state:
            st.success(st.session_state["msg"])
            del st.session_state["msg"]

        st.header("Confirmar Serviço")

        # --- Verifica se há profissional logado ---
        if "usuario_id" not in st.session_state:
            st.error("Nenhum profissional logado.")
            return
        
        id_profissional = st.session_state["usuario_id"]
        horarios = View.horario_filtrar_profissional(id_profissional)

        # --- Filtrar apenas horários que têm cliente e não estão confirmados ---
        horarios_disponiveis = [
            h for h in horarios 
            if h.get_id_cliente() is not None and h.get_confirmado() is False
        ]

        if len(horarios_disponiveis) == 0:
            st.info("Nenhum horário com cliente pendente de confirmação.")
            return
        
        # --- Lista horários disponíveis ---
        opcoes_horarios = []
        for h in horarios_disponiveis:
            cliente = View.cliente_listar_id(h.get_id_cliente())
            cliente_nome = cliente.get_nome() if cliente else "Desconhecido"
            opcoes_horarios.append(f"{h.get_id()} - {h.get_data()} - Cliente: {cliente_nome}")

        opcao_horario = st.selectbox("Selecione o horário para confirmar", opcoes_horarios)
        id_horario = int(opcao_horario.split(" - ")[0])
        horario = View.horario_listar_id(id_horario)

        # --- Botão de confirmação ---
        if st.button("Confirmar"):
            if horario is None:
                st.error("Horário inválido.")
                return

            if horario.get_id_cliente() is None:
                st.warning("Não é possível confirmar um horário sem cliente.")
                return

            horario.set_confirmado(True)
            View.horario_atualizar_obj(horario)

            # Mensagem persistente
            st.session_state["msg"] = "✅ Serviço confirmado com sucesso!"
            st.rerun()
