import streamlit as st
from views import View

class loginUI:
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")

        if st.button("Entrar"):
            c = View.cliente_autenticar(email, senha)
            p = View.profissional_autenticar(email, senha)

            if c == None and p == None: st.write("E-mail ou senha inválidos")
            
            else:
                if c is not None:
                    st.session_state["usuario_id"] = c["id"]
                    st.session_state["usuario_nome"] = c["nome"]
                    st.session_state["usuario_tipo"] = "cliente"
                else:
                    st.session_state["usuario_id"] = p["id"]
                    st.session_state["usuario_nome"] = p["nome"]
                    st.session_state["usuario_tipo"] = "profissional"
                
                st.success(f"Bem vindo(a), {st.session_state['usuario_nome']}!")
                st.rerun()
