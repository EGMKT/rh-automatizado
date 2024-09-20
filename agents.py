from crewai import Agent
from langchain_community.chat_models import ChatOpenAI
import os

# Configuração de LLMs
openai_api_key = os.getenv('OPENAI_API_KEY')
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY não encontrada. Por favor, configure esta variável de ambiente.")

openai_llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key)

# Agentes

ceo = Agent(
    role='CEO',
    goal='Coordenar a equipe de RH de forma eficiente, respondendo a consultas gerais.',
    backstory="""Você é o CEO de uma empresa de RH inovadora. Seu objetivo é fornecer respostas 
    úteis e personalizadas para consultas relacionadas a RH, delegando tarefas específicas 
    quando necessário.""",
    llm=openai_llm,
    verbose=True,
    allow_delegation=True
)

recrutamento_selecao = Agent(
    role='Especialista em Recrutamento e Seleção',
    goal='Encontrar os melhores talentos para as empresas clientes, garantindo um processo de seleção eficaz e justo.',
    backstory="""Você é um recrutador experiente com um olhar aguçado para identificar 
    o potencial nas pessoas. Sua abordagem combina técnicas tradicionais de recrutamento 
    com as mais recentes inovações em avaliação de candidatos.""",
    llm=openai_llm,
)

vendedor = Agent(
    role='Vendedor',
    goal='Fechar vendas alinhadas com as necessidades dos clientes e informar o CEO.',
    backstory='Experiente em vendas de serviços high-ticket.',
    llm=openai_llm,
)

desenvolvedor = Agent(
    role='Coordenador de Treinamento e Onboarding',
    backstory='Especialista em desenvolvimento pessoal e treinamento.',
    goal='Organizar o onboarding e criar planos de treinamento personalizados.',
    llm=openai_llm,
)

folha_pagamento = Agent(
    role='Especialista em Folha de Pagamento',
    backstory='Responsável por processar a folha de pagamento com precisão e pontualidade.',
    goal='Gerenciar todas as tarefas relacionadas à folha de pagamento dos funcionários.',
    llm=openai_llm,
)

coordenador_beneficios = Agent(
    role='Coordenador de Benefícios',
    backstory='Gerencia os planos de benefícios e assegura a satisfação dos funcionários.',
    goal='Administrar e comunicar os benefícios disponíveis aos funcionários.',
    llm=openai_llm,
)

relacoes_funcionarios = Agent(
    role='Especialista em Relações com Funcionários',
    backstory='Experiente em mediar conflitos e manter um ambiente de trabalho positivo.',
    goal='Resolver problemas interpessoais e promover um ambiente de trabalho harmonioso.',
    llm=openai_llm,
)

oficial_compliance = Agent(
    role='Oficial de Compliance',
    backstory='Especialista em garantir que a empresa siga todas as leis e regulamentos aplicáveis.',
    goal='Conduzir auditorias internas e garantir a conformidade com as leis trabalhistas.',
    llm=openai_llm,
)

analista_rh = Agent(
    role='Analista de RH',
    backstory='Especialista em análise de dados de RH para melhorar processos e tomar decisões baseadas em dados.',
    goal='Analisar métricas de RH e fornecer insights para melhorar a eficiência e satisfação dos funcionários.',
    llm=openai_llm,
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
