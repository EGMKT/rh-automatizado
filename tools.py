import os
import requests
import logging
import base64
from crewai_tools import BaseTool

# Ferramentas
class SearchCandidatesTool(BaseTool):
    name: str = "search_candidates"  # Adicione a anotação de tipo aqui
    description = "Searches for candidates based on a job title."

    def _run(self, job_title: str) -> str:
        api_url = "https://example.com/api/candidates"
        params = {"job_title": job_title}
        
        try:
            response = requests.get(api_url, params=params)
            response.raise_for_status()
            candidates = response.json()
            logging.info(f"Found {len(candidates)} candidates for {job_title}")
            return f"Found {len(candidates)} candidates: " + ", ".join([f"{c['name']} ({c['email']})" for c in candidates])
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching candidates: {e}")
            return "Error fetching candidates."

    def _arun(self, job_title: str):
        # This can be implemented for async execution if needed
        raise NotImplementedError("This tool does not support async execution")

def schedule_meeting_with_google_calendar(candidate_email: str, time: str, description: str):
    calendar_api_url = "https://www.googleapis.com/calendar/v3/calendars/primary/events"
    data = {
        "summary": "Entrevista de Trabalho",
        "description": description,
        "start": {"dateTime": time},
        "end": {"dateTime": time},  # Exemplo simples; ajustável para durar 1h, por exemplo
        "attendees": [{"email": candidate_email}],
    }

    headers = {"Authorization": f"Bearer {os.getenv('GOOGLE_API_KEY')}"}
    
    try:
        response = requests.post(calendar_api_url, json=data, headers=headers)
        response.raise_for_status()
        logging.info(f"Entrevista marcada com {candidate_email} para {time}")
        return f"Entrevista marcada com {candidate_email}"
    except requests.exceptions.RequestException as e:
        logging.error(f"Erro ao marcar entrevista: {e}")
        return "Erro ao marcar entrevista."

def send_email_via_gmail(to_email: str, subject: str, body: str):
    gmail_api_url = "https://www.googleapis.com/gmail/v1/users/me/messages/send"
    data = {
        "raw": base64.urlsafe_b64encode(f"To: {to_email}\nSubject: {subject}\n\n{body}".encode("utf-8")).decode("utf-8")
    }

    headers = {"Authorization": f"Bearer {os.getenv('GOOGLE_API_KEY')}"}
    
    try:
        response = requests.post(gmail_api_url, json=data, headers=headers)
        response.raise_for_status()
        logging.info(f"E-mail enviado para {to_email}")
        return f"E-mail enviado para {to_email}"
    except requests.exceptions.RequestException as e:
        logging.error(f"Erro ao enviar e-mail: {e}")
        return "Erro ao enviar e-mail."

def search_documents_on_google_drive(query: str):
    drive_api_url = "https://www.googleapis.com/drive/v3/files"
    params = {"q": f"name contains '{query}'", "fields": "files(id, name)"}
    headers = {"Authorization": f"Bearer {os.getenv('GOOGLE_API_KEY')}"}

    try:
        response = requests.get(drive_api_url, params=params, headers=headers)
        response.raise_for_status()
        files = response.json().get("files", [])
        logging.info(f"Documentos encontrados: {[file['name'] for file in files]}")
        return files
    except requests.exceptions.RequestException as e:
        logging.error(f"Erro ao buscar documentos: {e}")
        return "Erro ao buscar documentos."
