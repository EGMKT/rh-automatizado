from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv
from agents import *
from tasks import *
import os
from langchain_community.chat_models import ChatOpenAI 
from IPython.display import Markdown
import logging
from logging_config import setup_logging

# Carrega dotenv
load_dotenv()


# Inicializa o logging
setup_logging()
logging.info("Iniciando o sistema de RH automatizado com CrewAI.")

# API Keys 
openai_api_key=os.getenv('OPENAI_API_KEY')
openai_llm=ChatOpenAI(model='gpt-4', api_key=openai_api_key)



# Crews
crew_recrutamento = Crew(
    agents=[recrutamento_selecao, desenvolvedor],
    tasks=[recrutamento]
)

crew_vendas = Crew(
    agents=[vendedor],
    tasks=[vendas]
)

crew_operacoes = Crew(
    agents=[folha_pagamento, coordenador_beneficios, relacoes_funcionarios, oficial_compliance, analista_rh],
    tasks=[processar_folha, gestao_beneficios, mediacao_conflitos, auditoria_compliance, analise_dados]
)

crew_executiva = Crew(
    agents=[ceo],
    tasks=[delegacao]
)

# Iniciando o Enxame
all_crews = [crew_recrutamento, crew_vendas, crew_operacoes, crew_executiva]

for crew in all_crews:
    result = crew.kickoff()
    Markdown(result)
