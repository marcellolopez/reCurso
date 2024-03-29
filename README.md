# Herramienta de Automatización SQL

Esta herramienta utiliza Selenium y OpenAI para automatizar la navegación en el sitio web https://sqlinteractivo.desafiolatam.com/ y generar consultas SQL mediante la interacción con ChatGPT.

## Configuración

1. Asegúrate de tener Python instalado en tu máquina.
2. Instala las dependencias ejecutando `pip install -r requirements.txt`.
3. Descarga el [controlador del navegador Chrome](https://sites.google.com/chromium.org/driver/).
4. Crea un archivo `config.py` en el mismo directorio que los scripts con la siguiente estructura:

    ```python
    # config.py
    import os
    
    # Ingresar API Key de ChatGPT
    openai_api_key = "TU_CLAVE_DE_API_DE_CHATGPT_AQUÍ"
    
    # Ingresar correo y contraseña
    user = "correo@correo.com"
    passw = "password"
    ```

## Uso

1. Ejecuta el script `automation.py`.
2. Ingresa las credenciales cuando se solicite.
3. El script automatizará la navegación, consultará descripciones de pruebas y utilizará ChatGPT para generar consultas SQL.

## Estructura del Proyecto

- `automation.py`: Script principal para la automatización.
- `ChatGPT.py`: Módulo para interactuar con la API de ChatGPT.
- `funciones.py`: Módulo que contiene funciones comunes utilizadas en la automatización.

## Dependencias

- [Selenium](https://pypi.org/project/selenium/): Para la automatización del navegador.
- [OpenAI](https://beta.openai.com/signup/): Para la consulta a la API de ChatGPT.

## Registro de Actividades

Los detalles de la actividad y cualquier mensaje importante se registran en archivos de registro en la carpeta `logs`.

## Contribuciones

Si encuentras algún problema o deseas mejorar la herramienta, ¡siéntete libre de contribuir abriendo un problema o enviando un pull request!
