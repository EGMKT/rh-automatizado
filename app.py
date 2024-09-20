import streamlit as st
from dotenv import load_dotenv
import os
from crewai import Crew
from agents import recrutamento_selecao, desenvolvedor
from tasks import recrutamento

load_dotenv()

st.set_page_config(page_title="RH Automatizado", page_icon="👥")

st.title("RH Automatizado")

st.sidebar.success("Selecione uma função acima.")

def main():
    menu = ["Recrutamento", "Folha de Pagamento", "Gestão de Equipes", "Análise de Dados"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Recrutamento":
        st.subheader("Recrutamento")
        job_title = st.text_input("Título da vaga")
        if st.button("Recrutar"):
            crew_recrutamento = Crew(
                agents=[recrutamento_selecao, desenvolvedor],
                tasks=[recrutamento]
            )
            with st.spinner('Processando...'):
                result = crew_recrutamento.kickoff()
            st.success(result)

    elif choice == "Folha de Pagamento":
        st.subheader("Folha de Pagamento")
        # Adicione a lógica para folha de pagamento aqui

    elif choice == "Gestão de Equipes":
        st.subheader("Gestão de Equipes")
        # Adicione a lógica para gestão de equipes aqui

    elif choice == "Análise de Dados":
        st.subheader("Análise de Dados")
        # Adicione a lógica para análise de dados aqui

if __name__ == '__main__':
    main()