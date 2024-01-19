# funciones.py
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import os
import config

fecha = time.strftime("%Y%m%d_%H%M%S")
cadena_aleatoria = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
nombre_archivo = f"log_{fecha}_{cadena_aleatoria}"

service = webdriver.chrome.service.Service(executable_path='./chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome()


def iniciar_driver():
    limpiar_consola()
    imprimir("Iniciando driver")
    return driver

# Función que devuelva dos cadenas, user y pass 
def user_pass():
    user = config.user
    passw = config.passw
    return user, passw

def inicio_tiempo():
    global inicio_tiempo_global
    inicio_tiempo_global = time.time()

#función que hace el login
def login():
    limpiar_consola()
    imprimir("Haciendo login")

    driver.get("https://sqlinteractivo.desafiolatam.com/ingreso/login")

    ## Trae la función user_pass()
    user, passw = user_pass()

    # Introducir usuario y contraseña
    driver.find_element(By.ID, "email").send_keys(user)
    driver.find_element(By.ID, "password").send_keys(passw)

    # Hacer clic en el botón con el texto "Ingresar"
    boton_ingresar = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Ingresar']"))
    )
    imprimir("Ingresando...")
    boton_ingresar.click()

    # Esperar 5 segundos (puedes ajustar este tiempo según sea necesario)
    time.sleep(5)

# Función que cierra sesión
def logout():
    limpiar_consola()
    imprimir("Haciendo logout")
    
    # Encontrar el elemento del botón "Muné"
    boton_menu = driver.find_element(By.XPATH, "//html/body/nav/div/button")
    boton_menu.click()
    esperar(2)    
    
    # Encontrar el elemento del botón "Mi Perfil"
    boton_perfil = driver.find_element(By.XPATH, '//*[@id="navbarNavDropdown"]/ul/li[4]/div/button')
    boton_perfil.click()
    esperar(2)

    # Encontrar el elemento "Cerrar sesión" dentro del menú desplegable
    enlace_cerrar_sesion = driver.find_element(By.XPATH, "//div[@class='logout']/a")

    # Hacer clic en "Cerrar sesión"
    enlace_cerrar_sesion.click()

    time.sleep(3)

def esperar_carga_completa(xpath):
    imprimir(f"Esperando carga de elemento {xpath}")
    try:
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
    except TimeoutError:
        pass
        imprimir("La página no se cargó completamente en el tiempo especificado")


def mostrar_tiempo_transcurrido():
    limpiar_consola()
    if inicio_tiempo_global is not None:
        tiempo_transcurrido = time.time() - inicio_tiempo_global
        imprimir(f"Tiempo transcurrido: {round(tiempo_transcurrido, 2)} segundos")
    else:
        imprimir("El tiempo de inicio no ha sido establecido. Llama a 'inicio_tiempo()' primero.")

def esperar(segs):
    imprimir(f"Esperando {segs} segundos...")
    time.sleep(segs)

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

## función que haga scroll hacia abajo a la mitad de la página
def scrollDownHalf():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 3);")

def scrollDown():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def scrollUp():
    driver.execute_script("window.scrollTo(0, 0);")


def imprimir(texto):
    print(texto)
    guardarArchivoLog(texto)

def guardarArchivoLog(texto):

    fecha = time.strftime("%Y-%m-%d_%H:%M:%S")
    with open(f'logs/{nombre_archivo}.txt', 'a') as f:
        ## Setea variable fecha con el formato YYYY-MM-DD HH:MM:SS        
        f.write( f"[{fecha}] : " + texto + '\n')
        f.close()



