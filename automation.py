# automation.py
# reCurso
# Herramienta para contestar una prueba de SQL con Chat GPT

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException

#importar archivo chatGPT.py
import chatGPT

## importar el archivos funciones.py
from funciones import *


#declarar driver con la función iniciar_driver() y como variable global
driver = iniciar_driver()


#función para iniciar el tiempo de ejecución
inicio_tiempo()

#variable de respuestas correctas
respuestas_correctas = 0

#Variable preguntas realizadas
preguntas_realizadas = 0

login()

# Toma todos los elementos con el xpath "/html/body/div[2]/div[1]/ul" los recorre en un for
esperar_carga_completa("/html/body/div[2]/div[1]/ul//a")


# Toma todos los elementos con el xpath "/html/body/div[2]/div[1]/ul" y obtiene los <a>
enlaces = driver.find_elements(By.XPATH, "/html/body/div[2]/div[1]/ul//a")

# Devuelve cantidad de enlaces
cantidad_enlaces = len(enlaces)

# Con un for recorre todos los enlaces 1 a 1
for indice, enlace in enumerate(enlaces, start=1):
    limpiar_consola()
    imprimir("Entra al enlace")

    esperar(3)    

    imprimir('Probando indice')
    string = f"/html/body/div[2]/div[1]/ul/li[{indice}]/a"

    if indice > 6 and indice < 8 :
        

        # Ejecuta JavaScript para desplazarte a la mitad de la página
        scrollDownHalf()
        # espera 3 segundos
        esperar(3)

    elif indice > 8 and indice < 12:
        # Ejecuta JavaScript para desplazarte hasta el final de la página
        scrollDown()
        # espera 3 segundos
        esperar(3)
    

    esperar_carga_completa(string)
    driver.find_element(By.XPATH, string).click()

    # Ejecuta JavaScript para desplazarte hasta el inicio de la página
    scrollUp()
    
    #espera de 5 segundos
    esperar(5)

    # Toma todos los elementos con el xpath "/html/body/div[2]/div[2]/div[1]/ul" y obtiene el primer li
    elemento = driver.find_elements(By.XPATH, f"/html/body/div[2]/div[2]/div[{indice}]/ul/li")

    # Espera 2 segundos
    esperar(2)

    imprimir("Click en el elemento")
    elemento[0].click()

    # Espera 2 segundos
    esperar(2)
    

    # Bucle principal
    while driver.current_url != "https://sqlinteractivo.desafiolatam.com/categorias":
        limpiar_consola()
        try:
            # Ejecuta JavaScript para desplazarte hasta el final de la página
            scrollDown()            
            imprimir("Esperando elemento descripcion...") 
                                
            #esperar 2 segundos
            esperar(3)

            # tomo todo lo que se encuentra en la clase "descripcion"
            imprimir("Toma elemento descripcion")
            descripcion = driver.find_element(By.CLASS_NAME, "descripcion")

            # paso todos los elementos a un string
            descripcion_str = descripcion.text

            consulta = ""

            # usar la función de chatGPT llamada consultar()
            consulta = chatGPT.consultar(descripcion_str)

            # Formatear caracteres raros (puedes ajustar esta línea según sea necesario)
            consulta = consulta.encode('utf-8', 'ignore').decode('utf-8')

            # Ejecuta JavaScript para desplazarte hasta el final de la página
            scrollDown() 

            # Esperar 2 segundos
            esperar(3)

            # Haz clic en el elemento con la clase "boxEditor"
            elemento_box_editor = driver.find_element(By.CLASS_NAME, "inputarea")
            
            # Limpia el contenido de la textarea
            elemento_box_editor.clear()

            # Simula la escritura como si fuera un teclado en el elemento
            elemento_box_editor.send_keys(consulta)

            # Esperar 3 segundos
            esperar(3)

            # Presionar el botón de clase "queryButton"
            driver.find_element(By.CLASS_NAME, "queryButton").click()

            # Ejecuta JavaScript para desplazarte hasta el final de la página
            scrollDown()

            # Esperar 1 segundos
            esperar(1)

            # Verificar si existe un <h3> con el texto "Resultado Correcto"
            resultado = driver.find_elements(By.XPATH, "//h3[text()='Resultado Correcto']")
            
            # Incrementa el contador de preguntas realizadas y respuestas correctas si el resultado es True
            preguntas_realizadas = preguntas_realizadas + 1
            if resultado:
                respuestas_correctas = respuestas_correctas + 1

            imprimir("Hace click a botón Siguiente")
            try:
                boton = driver.find_element(By.XPATH, "/html/body/main/div[2]/div[4]/a[2]/button")         
                boton.click()
            except NoSuchElementException:  
                pass
                imprimir("No se encontró el botón Siguiente, regresando a Mis Categorías")
                driver.get("https://sqlinteractivo.desafiolatam.com/categorias") 
                # Espera 3 segundos
                esperar(3)

        except NoSuchElementException:
            pass
            esperar(3)
                
    logout()
    login()

    # Llama a la función para mostrar el tiempo transcurrido
    mostrar_tiempo_transcurrido()
    imprimir(f"Respuestas correctas: {respuestas_correctas}")


esperar(15)

# terminar programa
driver.quit()



