from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Task(BaseModel):
    """Modelo que representa una tarea individual"""
    id: Optional[int] = None
    title: str = Field(..., description="El nombre o descripción corta de la tarea")
    description: Optional[str] = Field(None, description="Detalles adicionales de la tarea")
    due_date: str = Field(..., description="Fecha límite (formato YYYY-MM-DD)")
    priority_level: int = Field(default=3, ge=1, le=5, description="Prioridad del 1 (baja) al 5 (crítica)")
    estimated_time_hours: float = Field(default=1.0, description="Tiempo estimado para completar")
    status: str = Field(default="pending", description="Estado: pending o completed")
    ai_recommendation: Optional[str] = Field(None, description="Comentario generado por la IA sobre esta tarea")
    
class TaskList(BaseModel):
    """Modelo para manejar la lista de tareas y su persistencia"""
    tasks: list[Task] = []