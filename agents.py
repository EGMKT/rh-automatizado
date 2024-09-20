from crewai import Agent
from tools import SearchCandidatesTool
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain_community.chat_models import ChatOpenAI
import os

# Configuração de LLMs
openai_llm = ChatOpenAI(model="gpt-4", api_key=os.getenv('OPENAI_API_KEY'))

# Instantiate tools
search_tool = SearchCandidatesTool

# Agentes

ceo = Agent(
    role='CEO',
    goal='Coordenar toda a equipe de forma eficiente, delegando tarefas conforme necessário.',
    backstory='Você fundou e gerencia uma empresa de RH que terceiriza serviços para outras empresas.',
    llm=openai_llm,
    verbose=True,
    allow_delegation=True
)

recrutamento_selecao = Agent(
    role='Recrutador',
    goal='Realizar o recrutamento e seleção de novos funcionários para empresas clientes.',
    backstory='Especialista em identificar talentos com as habilidades necessárias.',
    llm=openai_llm,
    tools=[search_tool],
    verbose=True
)

vendedor = Agent(
    role='Vendedor',
    goal='Fechar vendas alinhadas com as necessidades dos clientes e informar o CEO.',
    backstory='Experiente em vendas de serviços high-ticket.',
    llm=openai_llm,
    verbose=True
)

desenvolvedor = Agent(
    role='Coordenador de Treinamento e Onboarding',
    backstory='Especialista em desenvolvimento pessoal e treinamento.',
    goal='Organizar o onboarding e criar planos de treinamento personalizados.',
    llm=openai_llm,
    verbose=True
)

folha_pagamento = Agent(
    role='Especialista em Folha de Pagamento',
    backstory='Responsável por processar a folha de pagamento com precisão e pontualidade.',
    goal='Gerenciar todas as tarefas relacionadas à folha de pagamento dos funcionários.',
    llm=openai_llm,
    verbose=True
)

coordenador_beneficios = Agent(
    role='Coordenador de Benefícios',
    backstory='Gerencia os planos de benefícios e assegura a satisfação dos funcionários.',
    goal='Administrar e comunicar os benefícios disponíveis aos funcionários.',
    llm=openai_llm,
    verbose=True
)

relacoes_funcionarios = Agent(
    role='Especialista em Relações com Funcionários',
    backstory='Experiente em mediar conflitos e manter um ambiente de trabalho positivo.',
    goal='Resolver problemas interpessoais e promover um ambiente de trabalho harmonioso.',
    llm=openai_llm,
    verbose=True
)

oficial_compliance = Agent(
    role='Oficial de Compliance',
    backstory='Especialista em garantir que a empresa siga todas as leis e regulamentos aplicáveis.',
    goal='Conduzir auditorias internas e garantir a conformidade com as leis trabalhistas.',
    llm=openai_llm,
    verbose=True
)

analista_rh = Agent(
    role='Analista de RH',
    backstory='Especialista em análise de dados de RH para melhorar processos e tomar decisões baseadas em dados.',
    goal='Analisar métricas de RH e fornecer insights para melhorar a eficiência e satisfação dos funcionários.',
    llm=openai_llm,
    verbose=True
)

coordenador_beneficios = Agent(
    role="Coordenador de Benefícios",
    goal="Gerenciar os benefícios dos funcionários, assegurando a conformidade com as políticas da empresa.",
    backstory="Você é o responsável por garantir que todos os funcionários tenham acesso aos benefícios adequados.",
    llm=openai_llm,
    tools=[]  # Caso queira adicionar ferramentas para acesso de APIs de benefícios
)

relacoes_funcionarios = Agent(
    role="Especialista em Relações com Funcionários",
    goal="Promover a resolução de conflitos e melhorar o ambiente de trabalho.",
    backstory="Você é o ponto de contato para funcionários resolverem questões internas.",
    llm=openai_llm,
    tools=[]  # Futuras integrações podem ser adicionadas para pesquisa de bem-estar
)

oficial_compliance = Agent(
    role="Oficial de Compliance",
    goal="Garantir a conformidade com as normas trabalhistas e regulatórias.",
    backstory="Você monitora todas as atividades da empresa para assegurar que estão em conformidade com as leis.",
    llm=openai_llm,
    tools=[]  # Ferramentas de auditoria podem ser adicionadas no futuro
)
