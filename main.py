"""
INSTALACIONES Y ARCHIVOS NECESARIOS
--------------------

```shell
pip install rich
pip install pillow
```

- ✅ documentacion.md
- ✅ diagrama de flujo.jpg
"""
# PARA IMPRIMIR EN CONSOLA
from rich.markdown import Markdown
from rich.console import Console
from rich.panel import Panel
# PARA IMPRIMIR EN
import re
# Para abrir imágenes
from PIL import Image
# from matplotlib import pyplot as plt

# DEFINIR VARIABLES
# ------------------------------------------

# Para imprimir con formato en pantalla
console = Console(color_system='windows')

# Para enviar mensaje de error SI no se logra abrir documentacion.md
msj_error_carga_archivos = """
# [red]🚨ERROR🚨:  Ver Guia de ejecución (🔴ARCHIVOS NO CARGADOS🔴)[/red].

Este programa usa archivos externos. Verificar si cargaste los archivos correctos.

**Descargar la carpeta completa `📁 Entrega 1`  y ejecutar el programa**.

ARCHIVOS NECESARIOS
- ✅ "documentacion.md"
- 🌆 "diagrama de flujo.jpg"

Este programa necesita instalación de rich

```shell
pip install rich
```
"""

# ANOTACIONES PARA MOSTRAR DOCUMENTACION
# Documentación
contenido: str
# Variables de recorrido
header: int

# Bloques y contenido
bloques: list
titulos: list
bloque_elegido_hijos: list

# ANOTACIONES PARA MENSAJES
opciones: list
opcion: int
mensaje: str | None
panel_mensaje: Panel

# ABRIR DOCUMENTACION
# ------------------------------------------
def abrir_documento(ruta_doc: str) -> str:
    documento: str
    try:
        with open(ruta_doc, mode='r', encoding='utf-8') as file:
            documento = file.read()
    except Exception:
        # Si la documentación no abre, devolver "mensaje de error" en formato markdown
        documento = msj_error_carga_archivos
        
    return documento
    

# EXTRAER TITULOS
def extraer_titulos_md(contenido: str, cabecera: int) -> list:
    # Considerar el inicio del texto 
    # (.*) cualquier cosa 0 o +
    patron = fr'^#{{{cabecera}}} (.*)'
    titulos: list = re.findall(patron, contenido, flags=re.MULTILINE)
    return titulos

# EXTRAER BLOQUES DE TEXTO
def extraer_bloques_md(contenido: str, cabecera: int) -> list:
    # (^#{{{cabecera}}} Extraer desde el nivel de cabecera ingresada
    # .+?\n.*? es Extraer de 1 a mas de cualquier cosa que tenga abajo de 0 a más de cualquier cosa. Para considerar solo 1 salto de espacio en blanco
    # (...) Esto hará que extraigamos el patron de adentro. PAra eviarlo
    # (?=...). #{{1,{cabecera}}} esto no considerará desde 1 al nivel de header ingresado. sino tomará headers MENORES que no queremos
    patron = fr'(^#{{{cabecera}}} .+?\n.*?)(?=^#{{1,{cabecera}}} |\Z)'
    bloques: list = re.findall(patron, contenido, flags=re.MULTILINE | re.DOTALL)
    
    return bloques


def extraer_links_md(contenido: str) -> list:
    patron = r'\[.*\]\((.+?\.jpg|png)\)'
    links = re.findall(patron, contenido)
    
    return links
    
    
def colorear_texto_rich(texto: str, color: str = 'cyan', salto: bool = True) -> str:
    if color:
        nuevo_texto = f'[{color}]{texto}[/{color}]'
    if salto:
        nuevo_texto += '\n'
        
    return nuevo_texto


def generar_opciones(textos_opc: list, titulo_opc: str | None = None, clr_titulo_opc: str = 'yellow') -> list[list, str]:
    """
    # Uso
    `opciones` sirve para enumerar las opciones de la lista `mensaje`.
    >>> opciones = [1,2...]
    >>> textos_opc = ["1er texto","2do texto",...]
    
    # Ejemplo de uso
    >>> opciones, mensaje_opciones = generar_opciones(titulos)
    
    `opciones = [1,2...]`. Para acceder a los títulos:
    >>> opcion = opciones[0]
    
    corresponde a
    
    >>> textos_opc[opcion-1]
    """
    opciones_len: int = len(textos_opc)
    opciones: list[int] = list(range(1, opciones_len + 1))
    
    if not titulo_opc:
        titulo_opc = 'Elige una opción (Enteros. Ej.: 1)\n'
        
    mensaje: str = colorear_texto_rich(titulo_opc, clr_titulo_opc)
    
    for i in opciones:
        txt_opcion = f'{i:2}) {textos_opc[i-1]}'   
        mensaje += colorear_texto_rich(txt_opcion, 'green') 
    
    # Agregar opciones de Inicio y final
    txt_opcion_inicio = f'{opciones_len+1:2}) Inicio'
    txt_opcion_final = f'{opciones_len+2:2}) Cerrar programa'
    mensaje += colorear_texto_rich(txt_opcion_inicio, 'blue')
    mensaje += colorear_texto_rich(txt_opcion_final, 'red')
    opciones.append(opciones_len+1)
    opciones.append(opciones_len+2)
    
    return opciones, mensaje
    

def mostrar_contenido(contenido: str) -> None:
    # Imprimir contenido del bloque
    console.print('='*console.width, style='cyan')
    console.print(Markdown(contenido))
    console.print('='*console.width, style='cyan')
    
    links_images: list[str] = extraer_links_md(contenido)
    # mostrar imagen
    if links_images:
        for image in links_images:
            # PIL
            image_name = image.replace('%20', ' ')
            img = Image.open(image_name)
            img.show()
            
            # MATPLOTLIB
            # imagen_nombre = image.replace('%20', ' ')
            # console.print(Panel(imagen_nombre))
            # img = plt.imread(imagen_nombre)
            # plt.figure(figsize=(9,16))
            # plt.imshow(img)
            # plt.axis('off')
            # plt.show()
            
    console.input('Presiona ENTER para continuar...')
    
if __name__ == '__main__':
    header = 1
    documentacion = abrir_documento(ruta_doc='documentacion.md')
    contenido = documentacion
    # MOSTRAR DOCUMENTACION
    # ------------------------------------------
    
    while True:
        # Si no hay contenido en el archivo lanzar mensaje de error o cargar el texto con mensaje de error
        if not contenido:
            contenido = msj_error_carga_archivos
            continue
            
        titulos = extraer_titulos_md(contenido, header)
        
        opciones, mensaje = generar_opciones(titulos, clr_titulo_opc="#ffc400 underline")
        
        # MENSAJE PARA ELEGIR OPCIONES DE CONTENIDO
        # ------------------------------------------
        opcion: int | None = None
        while (opcion not in opciones) or (opcion is None):
            # Imprimir en panel
            panel_mensaje = Panel(mensaje, padding=(1,4))
            console.print(panel_mensaje)
            try:
                # Si recibir un entero para buscar en opciones
                opcion = int(console.input('Ingresar: '))
            except ValueError:
                # intentar de nuevo si hay excepcion de valor
                pass
        
        # FILTRAR POR OPCIONES EXTRAS
        # ------------------------------------------
        if opcion == opciones[-2]:
            contenido = documentacion
            header = 1
            continue
        elif opcion == opciones[-1]:
            break
                
        # LEER LOS CONTENIDOS
        # ------------------------------------------
        bloques: list = extraer_bloques_md(contenido, header)
        
        bloque_elegido = bloques[opcion-1]
        
        # MOSTRAR CONTENIDOS SI NO TIENE HIJOS
        # ------------------------------------------
        bloque_elegido_hijos = extraer_bloques_md(bloque_elegido, header+1)
        
        # Volver con bloque como seccion a analizar
        if bloque_elegido_hijos:
            contenido = bloque_elegido
            header = header + 1
            continue
        
        mostrar_contenido(bloque_elegido)
