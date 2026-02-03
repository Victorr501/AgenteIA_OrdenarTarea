from __future__ import annotations

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# 1.Cargar varialbes de entorno (.env)
load_dotenv()

def run() -> None:
    print("--- Iniciando Prueba de Conexión con Gemini ---")
    
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("ERROR: No se encontró la GOOGLE_API_KEY")
        return
    
    
    try:
        # Intentar una llamada directa
        llm = ChatGoogleGenerativeAI(
            model = "gemini-2.0-flash",
            google_api_key = api_key
        )
        response = llm.invoke("Hola, ¿estás activo?")
        print(f"\n Respuesta directa: {response.text}")
        print("\n --- ¡CONEXIÓN EXITOSA! ---")
        
    except Exception as e:
        print(f"\n Error de diagnóstico: {e}")


if __name__ == "__main__":
    run()
    
