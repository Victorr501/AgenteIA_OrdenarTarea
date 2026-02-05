from __future__ import annotations

class ArchivoNoEncontrado(Exception):
    """
    Se lanza cuando no se encuentra el archivo
    - Pedira el la ruta y te dira que archivo no esta creado.
    """
    def __init__(self, path):
        self.message = f"Error Crítico: El archivo de datos no existe en: {path}"
        super().__init__(self.message)
        
class NoEncotradaAPIIA(Exception):
    """
    Se lanaza cuando el programa no encuetra la API
    """
    def __init__(self, API):
        self.menssage = f"No se encontro ninguna API de: {API}"
        super().__init__(self.menssage)