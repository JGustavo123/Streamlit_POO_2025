import streamlit as st
import pandas as pd
from views import View

class ManterAvaliacaoUI:

    def main():
        st.title("⭐ Minhas Avaliações")
        ManterAvaliacaoUI.listar()

    def listar():
        id_profissional = st.session_state.get("usuario_id")

        if not id_profissional:
            st.warning("⚠️ Você precisa estar logado como profissional para ver suas avaliações.")
            return

        avaliacoes = View.avaliacao_listar()
        if not avaliacoes:
            st.info("Nenhuma avaliação encontrada.")
            return

        avaliacoes_profissional = [a for a in avaliacoes if a.get_id_profissional() == id_profissional]

        if not avaliacoes_profissional:
            st.info("Nenhuma avaliação para o seu perfil ainda.")
            return

        data = []
        for a in avaliacoes_profissional:
            cliente = View.cliente_listar_id(a.get_id_cliente())
            servico = View.servico_listar_id(a.get_id_servico())

            nome_cliente = cliente.get_nome() if cliente else f"Cliente {a.get_id_cliente()}"
            nome_servico = servico.get_descricao() if servico else f"Serviço {a.get_id_servico()}"

            data.append({
                "Cliente": nome_cliente,
                "Serviço": nome_servico,
                "Nota": a.get_nota(),
                "Comentário": a.get_comentario()
            })

        df = pd.DataFrame(data)

        media_nota = df["Nota"].mean()
        qtd_avaliacoes = len(df)

        col1, col2 = st.columns(2)
        with col1:
            st.metric("📊 Média das Notas", f"{media_nota:.1f}/5")
        with col2:
            st.metric("💬 Total de Avaliações", qtd_avaliacoes)

        st.divider()
        st.subheader("📋 Lista de Avaliações")
        st.dataframe(df, use_container_width=True)

    def avaliar():
        st.title("📝 Avaliar Profissional")

        id_cliente = st.session_state.get("usuario_id")
        if not id_cliente:
            st.warning("⚠️ Você precisa estar logado como cliente para avaliar um profissional.")
            return

        horarios = View.horario_listar()

        concluidos = [
            h for h in horarios
            if h.get_id_cliente() == id_cliente and h.get_confirmado() == True
        ]

        if not concluidos:
            st.info("📅 Você ainda não tem serviços concluídos para avaliar.")
            return

        opcoes = {}
        for h in concluidos:
            profissional = View.profissional_listar_id(h.get_id_profissional())
            servico = View.servico_listar_id(h.get_id_servico())

            nome_prof = profissional.get_nome() if profissional else f"Profissional {h.get_id_profissional()}"
            nome_serv = servico.get_descricao() if servico else f"Serviço {h.get_id_servico()}"
            data_formatada = h.get_data().strftime("%d/%m/%Y %H:%M") if h.get_data() else "Sem data"

            opcoes[f"{nome_serv} com {nome_prof} em {data_formatada}"] = h

        escolha = st.selectbox("Escolha o serviço concluído:", list(opcoes.keys()))
        horario = opcoes[escolha]

        nota = st.slider("⭐ Nota", 1, 5, 5)
        comentario = st.text_area("💬 Comentário (opcional)")

        if st.button("Enviar Avaliação"):
            View.avaliacao_inserir(
                horario.get_id_cliente(),
                horario.get_id_profissional(),
                horario.get_id_servico(),
                nota,
                comentario
            )
            st.success("✅ Avaliação enviada com sucesso!")
