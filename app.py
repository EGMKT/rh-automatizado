import streamlit as st
import os
from crewai import Crew
from agents import *
from tasks import *
from dotenv import load_dotenv
import tempfile

# Carregar variáveis de ambiente
load_dotenv()

# Configuração da página Streamlit
st.set_page_config(page_title="RH Automatizado", page_icon="👥", layout="wide")

# Título e introdução
st.title("🤖 Assistente de RH Automatizado")
st.markdown("""
    Olá! Sou seu assistente de RH inteligente. Como posso ajudar você hoje?
    Você pode me fazer perguntas sobre RH, solicitar análises ou até mesmo enviar documentos para revisão.
""")

# Sidebar com opções
with st.sidebar:
    st.title("🔧 Opções")
    task_type = st.selectbox(
        "Tipo de Tarefa",
        ["Geral", "Recrutamento", "Folha de Pagamento", "Gestão de Equipes", "Análise de Dados", "Benefícios", "Vendas", "Análise de Documento"]
    )
    
    # Opção para upload de arquivo
    uploaded_file = st.file_uploader("Envie um documento para análise", type=["pdf", "docx", "txt"])

# Função para processar o arquivo enviado
def process_uploaded_file(file):
    if file is not None:
        # Cria um arquivo temporário
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.name)[1]) as tmp_file:
            tmp_file.write(file.getvalue())
            tmp_file_path = tmp_file.name
        
        # Aqui você pode adicionar a lógica para analisar o arquivo
        # Por exemplo, usando um agente específico para análise de documentos
        crew = Crew(
            agents=[analista_rh],  # Supondo que temos um agente capaz de analisar documentos
            tasks=[Task(
                description=f"Analise o documento em {tmp_file_path} e forneça um resumo detalhado.",
                agent=analista_rh,
                expected_output="Um resumo detalhado do documento analisado."
            )]
        )
        result = crew.kickoff()
        
        # Não esqueça de remover o arquivo temporário após o uso
        os.unlink(tmp_file_path)
        
        return result
    return None

# Chat interface
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Digite sua pergunta ou tarefa aqui..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Lógica para selecionar a Crew apropriada
        if task_type == "Recrutamento":
            crew = Crew(agents=[recrutamento_selecao, desenvolvedor], tasks=[recrutamento])
        elif task_type == "Folha de Pagamento":
            crew = Crew(agents=[folha_pagamento], tasks=[processar_folha])
        elif task_type == "Gestão de Equipes":
            crew = Crew(agents=[relacoes_funcionarios], tasks=[mediacao_conflitos])
        elif task_type == "Análise de Dados":
            crew = Crew(agents=[analista_rh], tasks=[analise_dados])
        elif task_type == "Benefícios":
            crew = Crew(agents=[coordenador_beneficios], tasks=[gestao_beneficios])
        elif task_type == "Vendas":
            crew = Crew(agents=[vendedor], tasks=[vendas])
        else:
            crew = Crew(agents=[ceo], tasks=[delegacao])

        try:
            with st.spinner('Processando sua solicitação...'):
                result = crew.kickoff(inputs={"user_input": prompt})
                full_response = str(result)
            message_placeholder.markdown(full_response)
        except Exception as e:
            full_response = f"Desculpe, ocorreu um erro: {str(e)}"
            message_placeholder.error(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Processamento do arquivo enviado
if uploaded_file:
    st.write("Analisando o documento enviado...")
    analysis_result = process_uploaded_file(uploaded_file)
    if analysis_result:
        st.write("Análise do documento:")
        st.write(analysis_result)

# Footer
st.markdown("---")
st.markdown("Desenvolvido com ❤️ por EverGreen MKT 🌲 usando Streamlit e CrewAI")

# Implementação das funções para selecionar agentes e tarefas apropriados
def get_agent_for_task(task_type):
    if task_type == "Recrutamento":
        return recrutamento_selecao
    elif task_type == "Folha de Pagamento":
        return folha_pagamento
    # ... outros casos ...
    else:
        return ceo

def get_task_for_type(task_type):
    if task_type == "Recrutamento":
        return recrutamento
    elif task_type == "Folha de Pagamento":
        return processar_folha
    # ... outros casos ...
    else:
        return delegacao