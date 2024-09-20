import streamlit as st
import os
from crewai import Crew
from agents import *
from tasks import *
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Desativar o file watcher do Streamlit
os.environ['STREAMLIT_SERVER_FILE_WATCHER_TYPE'] = 'none'

# Configurar variáveis de ambiente para limitar o uso de recursos
os.environ['STREAMLIT_SERVER_MAX_UPLOAD_SIZE'] = '5'
os.environ['STREAMLIT_SERVER_MAX_MESSAGE_SIZE'] = '50'

st.set_page_config(page_title="RH Automatizado", page_icon="👥", layout="wide")

# Título
st.title("RH Automatizado - Assistente de IA")

# Inicialização do histórico de mensagens
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibição do histórico de mensagens
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input do usuário
if prompt := st.chat_input("Como posso ajudar você hoje?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Lógica para selecionar a Crew apropriada
        if any(keyword in prompt.lower() for keyword in ["recrutar", "contratação", "vaga"]):
            crew = Crew(agents=[recrutamento_selecao, desenvolvedor], tasks=[recrutamento])
        elif "folha de pagamento" in prompt.lower():
            crew = Crew(agents=[folha_pagamento], tasks=[processar_folha])
        elif any(keyword in prompt.lower() for keyword in ["equipe", "funcionários", "conflito"]):
            crew = Crew(agents=[relacoes_funcionarios], tasks=[mediacao_conflitos])
        elif any(keyword in prompt.lower() for keyword in ["análise", "dados", "relatório"]):
            crew = Crew(agents=[analista_rh], tasks=[analise_dados])
        elif "benefícios" in prompt.lower():
            crew = Crew(agents=[coordenador_beneficios], tasks=[gestao_beneficios])
        elif "vendas" in prompt.lower():
            crew = Crew(agents=[vendedor], tasks=[vendas])
        else:
            crew = Crew(agents=[ceo], tasks=[delegacao])

        try:
            result = crew.kickoff()
            full_response = str(result)
        except Exception as e:
            full_response = f"Desculpe, ocorreu um erro: {str(e)}"

        message_placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Sidebar
st.sidebar.title("Informações")
st.sidebar.info("Este é um assistente de IA para automação de RH. Ele pode ajudar com recrutamento, folha de pagamento, gestão de equipes, análise de dados e muito mais.")