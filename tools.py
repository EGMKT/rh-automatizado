import requests
from crewai_tools import BaseTool
import os
from typing import List, Optional
from pydantic import Field

# Ferramentas
class LinkedInSearchTool(BaseTool):
    name = "linkedin_search"
    description = "Search for candidates on LinkedIn based on job titles and skills."

    def _run(self, job_title: str, skills: list) -> str:
        access_token = os.getenv('LINKEDIN_API_KEY')
        if not access_token:
            return "Erro: LINKEDIN_API_KEY não configurada."
        
        api_url = "https://api.linkedin.com/v2/jobSearch"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "X-Restli-Protocol-Version": "2.0.0"
        }
        params = {
            "keywords": job_title,
            "skills": ",".join(skills),
        }
        try:
            response = requests.get(api_url, headers=headers, params=params)
            response.raise_for_status()
            jobs = response.json().get("elements", [])
            return f"Found {len(jobs)} job postings related to {job_title}"
        except requests.RequestException as e:
            return f"Error in LinkedIn search: {e}"

class TrainingRecommendationTool(BaseTool):
    name: str = Field(default="training_recommendation")
    description: str = Field(default="Suggests training modules based on employee performance.")

    def _run(self, employee_performance: dict) -> str:
        # Based on performance, suggest training modules
        if employee_performance["rating"] < 3:
            return "Recommend basic training modules."
        elif employee_performance["rating"] >= 3 and employee_performance["rating"] < 4:
            return "Recommend intermediate training modules."
        else:
            return "Recommend advanced training modules."

class SalaryAnalysisTool(BaseTool):
    name: str = Field(default="salary_analysis")
    description: str = Field(default="Analisa tendências salariais para diferentes posições.")

    def _run(self, position: str) -> str:
        # Simule uma análise de salário aqui
        return f"A média salarial para a posição de {position} é de R$ X.XXX,XX, com variação de 15% dependendo da experiência e localização."

class PerformanceEvaluationTool(BaseTool):
    name: str = Field(default="performance_evaluation")
    description: str = Field(default="Avalia o desempenho dos funcionários com base em métricas predefinidas.")

    def _run(self, employee_data: dict) -> str:
        # Simule uma avaliação de desempenho aqui
        score = sum(employee_data.values()) / len(employee_data)
        return f"Com base nas métricas fornecidas, o desempenho do funcionário é classificado como {'Excelente' if score > 8 else 'Bom' if score > 6 else 'Precisa melhorar'}."