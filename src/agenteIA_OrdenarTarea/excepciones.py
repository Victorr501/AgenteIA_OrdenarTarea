class ArchivoNoEncontrado(Exception):
    """
    Se lanza cuando no se encuentra el archivo
    - Pedira el la ruta y te dira que archivo no esta creado.
    """
    def __init__(self, path):
        self.message = f"Error Crítico: El archivo de datos no existe en: {path}"
        super().__init__(self.message)