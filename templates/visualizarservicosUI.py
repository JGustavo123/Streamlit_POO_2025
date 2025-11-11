import streamlit as st
from views import View
import pandas as pd
import time

class VisualizarServicosUI:
    
    def main():
        st.header("Meus Serviços")

        # Verifica se o cliente está logado
        if "usuario_id" not in st.session_state:
            st.error("Nenhum cliente logado.")
            return

        id_cliente = st.session_state["usuario_id"]
        horarios = View.horario_filtrar_cliente(id_cliente)

        if len(horarios) == 0:
            st.info("Nenhum serviço agendado ainda.")
        else:
            dados = []
            for h in horarios:
                profissional = View.profissional_listar_id(h.get_id_profissional())
                servico = View.servico_listar_id(h.get_id_servico())

                dados.append({
                    "ID": h.get_id(),
                    "Data": h.get_data().strftime("%d/%m/%Y %H:%M") if h.get_data() else "",
                    "Confirmado": True if h.get_confirmado() else False,
                    "Profissional": profissional.get_nome() if profissional else None,
                    "Serviço": servico.get_descricao() if servico else None
                })

            df = pd.DataFrame(dados)
            st.dataframe(df, use_container_width=True)

            st.subheader("Encerrar Serviço")
            opcoes = [f"{d['ID']} - {d['Serviço']} ({d['Data']})" for d in dados]
            if len(opcoes) > 0:
                selecao = st.selectbox("Selecione o serviço finalizado", opcoes)
                if st.button("Encerrar e Avaliar"):
                    id_servico = int(selecao.split(" - ")[0])
                    horario = next((h for h in horarios if h.get_id() == id_servico), None)

                    if horario:
                        id_profissional = horario.get_id_profissional()
                        id_servico = horario.get_id_servico()

                        st.success("Serviço encerrado com sucesso!")
                        time.sleep(1)

                        st.write("### ⭐ Avaliar Profissional")
                        nota = st.slider("Nota (1 a 5)", 1, 5, 5)
                        comentario = st.text_area("Comentário (opcional)")

                        if st.button("Enviar Avaliação"):
                            try:
                                View.avaliacao_inserir(
                                    id_cliente,
                                    id_profissional,
                                    id_servico,
                                    nota,
                                    comentario
                                )
                                st.success("Avaliação enviada com sucesso!")
                                time.sleep(2)
                                st.rerun()
                            except Exception as e:
                                st.error(f"Erro ao enviar avaliação: {e}")
