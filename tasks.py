from crewai import Task
from agents import *
# Tasks
recrutamento = Task(
    description="""Conduza um processo completo de recrutamento para uma posição de desenvolvedor full-stack.
    1. Analise o mercado de trabalho atual para desenvolvedores.
    2. Crie uma descrição de vaga atrativa e detalhada.
    3. Defina critérios de seleção claros.
    4. Sugira canais para divulgação da vaga.
    5. Proponha um processo de triagem eficiente.
    6. Liste os top 5 candidatos com justificativas.""",
    expected_output='Um relatório detalhado do processo de recrutamento, incluindo análise de mercado, descrição da vaga, critérios de seleção, estratégia de divulgação, processo de triagem e lista dos top 5 candidatos.',
    agent=recrutamento_selecao
)


vendas = Task(
    description='Fechar um contrato de serviços de RH com uma nova empresa cliente.',
    expected_output='Contrato assinado e detalhes do novo cliente.',
    agent=vendedor
)


delegacao = Task(
    description="""
    Analise a entrada do usuário e responda de forma natural e concisa.
    Se for uma saudação, responda de forma amigável.
    Se for uma pergunta ou tarefa específica, forneça uma resposta relevante ou indique que vai delegar para um especialista.
    """,
    expected_output="Uma resposta adequada à entrada do usuário",
    agent=ceo
)

processar_folha = Task(
    description='Processar a folha de pagamento mensal para todos os funcionários, incluindo cálculos de impostos e benefícios.',
    expected_output='Relatório detalhado da folha de pagamento, incluindo salários, deduções e total de gastos da empresa.',
    agent=folha_pagamento
)

gestao_beneficios = Task(
    description='Revisar e atualizar o pacote de benefícios dos funcionários.',
    expected_output='Proposta de novos benefícios e análise de custos.',
    agent=coordenador_beneficios
)

mediacao_conflitos = Task(
    description='Mediar um conflito entre dois funcionários de departamentos diferentes.',
    expected_output='Relatório da mediação e plano de ação para resolução do conflito.',
    agent=relacoes_funcionarios
)

auditoria_compliance = Task(
    description='Conduzir uma auditoria interna de conformidade com as leis trabalhistas.',
    expected_output='Relatório de auditoria com recomendações de melhorias.',
    agent=oficial_compliance
)

analise_dados = Task(
    description='Analisar dados para melhorar processos de RH.',
    expected_output='Relatório com insights e recomendações.',
    agent=analista_rh,
    output_file='analise_dados_rh.pdf'
)

gestao_beneficios = Task(
    description="Verificar e ajustar os benefícios dos funcionários para o próximo ciclo de pagamento.",
    expected_output="Relatório completo dos benefícios ajustados.",
    agent=coordenador_beneficios
)
