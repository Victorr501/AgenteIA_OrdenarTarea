import json
import os
from pathlib import Path
from src.agenteIA_OrdenarTarea.models import Task, TaskList
from agenteIA_OrdenarTarea.excepciones import ArchivoNoEncontrado

class TaskDatabase:
    """Clase para gestionar la lectura y escritura de tareas en un archivo JSON."""
    
    def __init__(self, file_path: str = "data/tasks.json"):
        self.file_path = Path(file_path)
        if not self.file_path.exists():
            raise ArchivoNoEncontrado(self.file_path)
        
    def load_tasks(self)-> TaskList:
        """Carga las tareas; si el archivo está vacio devuelve una lsita vacía."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return TaskList(**data)
        except json.JSONDecodeError:
            return TaskList(tasks=[])
        
    def _save_to_disk(self, task_list: TaskList) -> None:
        """Escribe en el archivo JSON (requiere permisos de escritura)."""
        with open(self.file_path, "w", encoding="utf-8") as f:
            f.write(task_list.model_dump_json(indent=4))
            
    def add_task(self, task: Task) -> None:
        """Añade una tarea y persiste los cambios."""
        current_data = self.load_tasks()
        # Lógica de ID autoincremental simple
        task.id = max([t.id for t in current_data.tasks], default=0) + 1
        current_data.tasks.append(task)
        self._save_to_disk(current_data)
        
    def delete_task(self, task_id: int) -> bool:
        """Elimina una tarea por ID"""
        current_data = self.load_tasks()
        original_count = len(current_data.tasks)
        current_data.tasks = [t for t in current_data.tasks if t.id != task_id]
        
        if len(current_data.tasks) < original_count:
            self._save_to_disk(current_data)
            return True
        return False