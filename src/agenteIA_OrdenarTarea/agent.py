import os
from datetime import datetime
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from .models import Task, TaskList

class PriorityAgent:
    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY no configurada.")
        
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            google_api_key=api_key,
            temperature=0
        )
        self.structured_llm = self.llm.with_structured_output(Task)

    def parse_task_from_text(self, user_input: str) -> Task:
        """Extrae datos y genera recomendación en UN SOLO PROMPT para ahorrar cuota."""
        fecha_actual = datetime.now().strftime("%Y-%m-%d")

        system_prompt = (
            f"Hoy es {fecha_actual}. Extrae la información de la tarea del usuario. "
            "IMPORTANTE: En el campo 'ai_recommendation', incluye un consejo de "
            "productividad de máximo 15 palabras basado en la urgencia y prioridad."
        )

        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("user", "{input}")
        ])

        chain = prompt | self.structured_llm
        
        # Invocación única: Ahorramos 1 llamada a la API
        return chain.invoke({"input": user_input})

    def get_organized_plan(self, task_list: TaskList) -> str:
        """Planificación general."""
        if not task_list.tasks:
            return "No hay tareas para analizar."

        contexto = "\n".join([f"- {t.title} (Prio: {t.priority_level})" for t in task_list.tasks])
        
        prompt = ChatPromptTemplate.from_template(
            "Eres un coach. Ordena estas tareas por importancia y justifica brevemente:\n{tareas}"
        )
        
        chain = prompt | self.llm
        return chain.invoke({"tareas": contexto}).content