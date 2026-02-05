# AgenteIA_OrdenarTarea

Proyecto en Python para gestionar tareas y conectarse a Gemini (Google Generative AI) para asistir en la priorización.

## Características

- Modelo de tarea con validación de datos usando **Pydantic**.
- Persistencia en archivo JSON (`data/tasks.json`).
- Operaciones base de datos simples:
  - Cargar tareas.
  - Añadir tareas (con ID autoincremental).
  - Eliminar tareas por ID.
- Script de prueba para validar conexión con Gemini usando `GOOGLE_API_KEY`.

## Estructura del proyecto

```text
.
├── data/
│   └── tasks.json
├── src/agenteIA_OrdenarTarea/
│   ├── main.py         # Prueba de conexión con Gemini
│   ├── models.py       # Modelos Task y TaskList
│   ├── database.py     # Lectura/escritura de tareas en JSON
│   └── excepciones.py  # Excepciones personalizadas
├── pyproject.toml
└── requirements.txt
```

## Requisitos

- Python **3.11+**
- Una API key de Google AI Studio para Gemini (`GOOGLE_API_KEY`)

## Instalación

1. Clona el repositorio.
2. Crea y activa un entorno virtual.
3. Instala dependencias.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> Alternativa con `pyproject.toml`:

```bash
pip install -e .
```

## Configuración

Crea un archivo `.env` en la raíz del proyecto con:

```env
GOOGLE_API_KEY=tu_api_key_aqui
```

## Cómo usarlo

### 1) Probar conexión con Gemini

Ejecuta:

```bash
python -m src.agenteIA_OrdenarTarea.main
```

o, si instalaste el proyecto como paquete:

```bash
agenteIA-ordenarTarea
```

Salida esperada (resumen):

- Mensaje de inicio.
- Respuesta de Gemini.
- Confirmación de conexión exitosa.

Si no tienes la variable de entorno configurada, verás:

- `ERROR: No se encontró la GOOGLE_API_KEY`

### 2) Usar la base de datos de tareas desde código

Ejemplo rápido:

```python
from src.agenteIA_OrdenarTarea.database import TaskDatabase
from src.agenteIA_OrdenarTarea.models import Task

db = TaskDatabase("data/tasks.json")

task = Task(
    title="Terminar README",
    description="Documentar instalación y uso",
    due_date="2026-12-31",
    priority_leve=4,
    estimated_time_hours=2.5
)

db.add_task(task)
print("Tarea añadida")

tasks = db.load_tasks()
print(tasks)

ok = db.delete_task(1)
print("Eliminada:" , ok)
```

## Notas

- El campo `priority_leve` se encuentra con ese nombre en el modelo actual.
- `data/tasks.json` debe existir; si no existe, se lanzará una excepción personalizada.
- Si el JSON está vacío o inválido, la carga devuelve una lista vacía.

## Próximos pasos sugeridos

- Añadir comandos CLI para CRUD completo.
- Incluir ordenación automática por prioridad/fecha.
- Agregar pruebas unitarias para modelos y persistencia.

## Licencia

Pendiente de definir.
