from crewai import Task
from agents import *
# Tasks
recrutamento = Task(
    description='Recrutar novos funcionários para uma posição de desenvolvedor full-stack. Analise o mercado, crie uma descrição da vaga e liste os melhores candidatos.',
    expected_output='Lista detalhada de candidatos qualificados, incluindo suas habilidades principais e experiência relevante.',
    agent=recrutamento_selecao
)


vendas = Task(
    description='Fechar um contrato de serviços de RH com uma nova empresa cliente.',
    expected_output='Contrato assinado e detalhes do novo cliente.',
    agent=vendedor
)


delegacao = Task(
    description='Delegar tarefas para a equipe e supervisionar o progresso.',
    expected_output='Relatório de progresso das tarefas delegadas.',
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
