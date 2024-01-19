# ChatGPT.py
import os
from openai import OpenAI
import unicodedata  # Agrega esta línea
import json
import config
from openai import OpenAI




key = config.openai_api_key

# gets API Key from environment variable openai_api_key
client = OpenAI(api_key=key)


def consultar(ejercicio):
    print('Consultando con ChatGPT')
    try:
                                                                               
        tarea = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": "necesito que de los textos que te iré entregando me devuelvas el ejercicio, solamente la query que corresponde, sin otra palabra, solo la query. Si viene mas de una, devuelveme las queries en el mismo script: " + ejercicio,
                },
            ],
        )
        respuesta = tarea.choices[0].message.content
        print('Respuesta')
        print(respuesta)
        return respuesta
    
    except Exception as e:
        print(f"Error al generar consulta: {e}")
        return None

def consultar_nuevamente(ejercicio):
    try:
                                                                               
        tarea = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": "El resultado es incorrecto, intentalo de nuevo, agrega lo que falta y devuelve solo la query: " + ejercicio,
                },
            ],
        )
        respuesta = tarea.choices[0].message.content
        print(respuesta)
        return respuesta
    
    except Exception as e:
        print(f"Error al generar consulta: {e}")
        return None