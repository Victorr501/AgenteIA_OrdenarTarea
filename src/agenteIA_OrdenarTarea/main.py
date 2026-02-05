from __future__ import annotations

import os
import sys
from dotenv import load_dotenv

from .database import TaskDatabase
from .agent import PriorityAgent
from .excepciones import ArchivoNoEncontrado

load_dotenv()

def mostrar_menu() -> str:
    print(
        "\n" + "="*40 + "\n" +
        "       AGENTE IA: GESTOR ESTRATÉGICO         \n" +
        "="*40 + "\n" + 
        "1 . Añadir nueva tarea\n" +
        "2 . Ver organización recomendada\n" +
        "3 . Completar/Eliminar tarea\n" +
        "4 . Ver listado simple(JSON)\n" +
        "5 . Salir\n"+
        "="*40 + "\n"
        )
    return input("Seleciona una opción (1-5): ")

def mostrar_list_task(list_task) -> None:
    print("\n--- LISTADO DE TAREAS REGISTRADAS ---")
    if not list_task.tasks:
        print("No hay tareas pendientes.")
    for t in list_task.tasks:
        print(f"ID {t.id}: {t.title} (Vence: {t.due_date} | Prio: {t.priority_level})")

def run():
    try:
        db = TaskDatabase("data/tasks.json")
        agent = PriorityAgent()
        
        encendido = True
        while encendido:
            respuesta = mostrar_menu()
            
            match respuesta:
                case "1":
                    print("\n[IA] Describe qué tienes que hacer:")
                    texto_usuario = input("> ")
                    print("\n... El agente está analizando y parametrizando la informacion...")
                    
                    nueva_tarea = agent.parse_task_from_text(texto_usuario)
                    db.add_task(nueva_tarea)
                    
                    print(f"\nTarea guardada con éxito.")
                    print(f"Titulo: {nueva_tarea.title}")
                    print(f"Fecha: {nueva_tarea.due_date} | Prioridad: {nueva_tarea.priority_level}")
                    print(f"Consejo IA: {nueva_tarea.ai_recommendation}")
                case "2":
                    print("\n... Generando plan de priorización con Gemini ...")
                    
                    tareas = db.load_tasks()
                    plan = agent.get_organized_plan(tareas)
                    
                    print(f"\n--- RECOMENDACIÓN ESTRATÉGICA ---\n")
                    print(plan)
                    input("-"*200)
                case "3":
                    lista_tareas = db.load_tasks()
                    mostrar_list_task(list_task=lista_tareas)
                    
                    id_eliminar = input("\nIntroduce el ID de la tarea completada (Para cancelar 'esc'): ")
                    
                    if id_eliminar == "esc" or id_eliminar == "ESC":
                        pass
                    elif id_eliminar.isdigit() and db.delete_task(int(id_eliminar)):
                        print(f"Tarea {id_eliminar} marcada como completada y eliminada.")
                    else:
                        print("Error: ID no encontrado o formato inválido.")
                case "4":
                    lista_tareas = db.load_tasks()
                    mostrar_list_task(list_task=lista_tareas)
                    input("-"*200)
                case "5":
                    print("\nCerrando Agente IA. !Que tengas un día productivo!")
                    encendido = False
                case _:
                    print("\nOpción no reconocida. Inténtalo de nuevo")
                
    except ArchivoNoEncontrado as e:
        print(f"\nCRITICO: {e}")
    except Exception as e:
        print(f"\nError inesperado: {e}")
        
if __name__ == "__main__":
    run()