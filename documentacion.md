# Documentación

## Tema, problema y solución

**Tema**
Análisis de clientes y productos para la personalización y segmentación de grupos de clientes por preferencias de compra.

**Problema**
La tienda visualiza los datos de sus clientes y sus compras que impiden conocer las preferencias de sus clientes y sus propios productos. Esto tiene una influencia negativa en las ventas ya que no se puede realizar estrategias en el punto venta como las _ventas cruzadas_ o ventas por recomendaciones personalizadas.

**Solución**:
Se desarrollará una aplicación de análisis de datos y un sistema de visualización automática para observar las preferencias de productos y grupo de productos de los clientes. Mediante el análisis de preferencias compartidas se segmentará a los clientes.
- **Información a analizar**
	- Categorías preferidas de clientes
	- Relación de grupos de productos y clientes
	- Relación de grupos de productos y ciudades de clientes
	- Análisis de dinero gastado por cliente
	- Análisis del tipo de pago y los segmentos de clientes
	- Análisis de la relación de dinero gastado y segmentos de clientes.


## Tablas de datasets

Fuente, definición, estructura, tipos y escala.

### Tabla Clientes

- **Tabla**: clientes
- **Archivo**: `clientes.csv`
- **Definición**: Esta tabla contiene información básica de los clientes.

| Llave | Campo          | Tipo de dato (py) | Escala    | Detalles                                 |
| ----- | -------------- | ----------------- | --------- | ---------------------------------------- |
| PK    | id_cliente     | int               | Nominal   |                                          |
|       | nombre_cliente | str               | Nominal   | Nombre + Apellido. Ejemplo: Bruno Castro |
|       | email          | str               | Nominal   | Correo del cliente                       |
|       | ciudad         | str               | Nominal   | Ciudad del cliente                       |
|       | fecha_alta     | datetime          | Intervalo | Fecha de registro                        |

### Tabla Detalle de ventas

- **Tabla**: detalle_ventas
- **Archivo**: `detalle_ventas.csv`
- **Definición**: Es la relación entre ventas y productos ya que 1 venta puede tener varios productos.

| Llave | Campo                                      | Tipo de dato (py) | Escala  | Detalles                                                      |
| ----- | ------------------------------------------ | ----------------- | ------- | ------------------------------------------------------------- |
| FK    | id_venta                                   | int               | Nominal | Relación a tabla productos                                    |
| FK    | id_producto                                | int               | Nominal | Relación a tabla productos                                    |
|       | nombre_producto                            | str               | Nominal | OBSERVACIÓN: Campo de tabla producto                          |
|       | precio_unitario                            | float             | Razón   | OBSERVACIÓN: Campo de tabla producto                          |
|       | cantidad                                   | int               | Razón   | Cantidad del mismo producto en una venta                      |
|       | importe                                    | float             | Razón   | precio_unitario x cantidad                                    |
| PK    | (id_venta, id_producto) o id_detalle_venta | int               | Nominal | Solo la combinación id_venta y id_producto no puede repetirse |

### Tabla Ventas

- **Tabla**: ventas
- **Archivo**: `ventas.csv`
- **Definición**: Las ventas sucede cuando los clientes compran 1 o más productos en una fecha determinada y con algún medio de pago.

| Llave | Campo          | Tipo de dato (py) | Escala    | Detalles                                       |
| ----- | -------------- | ----------------- | --------- | ---------------------------------------------- |
| PK    | id_venta       | int               | Nominal   | Relación a tabla ventas                        |
| FK    | id_cliente     | int               | Nominal   | Relación a tabla clientes                      |
|       | fecha          | datetime          | Intervalo | Debería ser fecha y hora                       |
|       | nombre_cliente | str               | Nominal   | OBSERVACIÓN: Campo de tabla clientes           |
|       | email          | str               | Nominal   | OBSERVACIÓN: Campo de tabla clientes           |
|       | medio_pago     | str               | Nominal   | Opciones: tarjeta, qr, transferencia, efectivo |

### Tabla Productos

- **Tabla**: productos
- **Archivo**: `productos.csv`
- **Definición**: Son los artículos que vende la empresa.

| Llave | Campo           | Tipo de dato (py) | Escala  | Detalles                             |
| ----- | --------------- | ----------------- | ------- | ------------------------------------ |
| PK    | id_producto     | int               | Nominal |                                      |
|       | nombre_producto | str               | Nominal | El nombre                            |
|       | categoria       | str               | Nominal | Opciones: Alimentos, Limpieza        |
|       | precio_unitario | float             | Razón   | El precio de cada unidad de producto |

## Información y lógica

### Descripción y pasos

**Información**: Este debe leer un archivo Markdown, mostrando como opciones sus títulos para seleccionarlos y ver el contenido.

**Pasos**:
- Debe identificar cada "header" de nivel 1 e imprimir sus títulos como opciones.
- Si el usuario elige uno sin títulos "hijos" debe mostrar el contenido, si tiene hijos debe mostrar sus títulos como opciones.

### Pseudocódigo

1. **Inicio**
2. **Definir** contenido como _Cadena_
3. **Abrir** "documentación.md"
4. **Interpretar** "documentación.md" como _Cadena_. **Asignarlo** `documentación`
5. `contenido` = `documentación`
6. **Mientras** Verdadero **hacer**
	1. **Declarar** `opciones` como _Lista_
	2. **Declarar** `mensaje` como _Cadena_
	3. `mensaje` = "Ingresa una opción (número entero)"
	4. **Interpretar** los títulos de máximo nivel de `contenido` como _Lista_. **Asignarlo** a `títulos`
	5. **Si** `contenido` está vacío
		1. **Asignar** "mensaje de error" a `contenido`
		2. **Continuar siguiente iteración**
	6. **Sino-Si** `titulo` está vacío
		1. **Concatenar** "mensaje de error" y `contenido`. **Asignarlo** a `contenido`
		2. **Continuar siguiente iteración**
	7. `opciones` = `titulos`
	8. **Agregar** 2 opciones a `opciones` para "inicio" y "cierre"
	9. **Interpretar** `opciones` como _Cadena_ de lista numerada. **Asignarlo** a `mensaje`
	10. **Mientras** `opcion` no existe o no está en `opciones`
		1. **Imprimir** `mensaje`
		2. **Leer** `opcion`
	11. **Fin-Mientras**
	12. **Si** `opcion` == `opciones[-1]`:
		1. **Terminar-Mientras**
	13. **Sino-Si** `opcion` == `opciones[-2]«
		1. `contenido` = `documentacion`
		2. **Continuar siguiente iteración**
	14. **Interpretar** `contenido` como _Lista_ de bloques separados por las "cabeceras" de nivel máximo. **Asignarlo** a `bloques`
	15. `bloque_elegido` = `bloques[opcion-1]`
	16. **Si** `bloque_elegido` tiene "sub-cabeceras":
		1. `contenido` = `bloque_elegido`
		2. **Continuar siguiente iteración**
	17. **Sino**
		1. **Imprimir** `bloque_elegido`
7. **Fin-Mientras**
8. **Final**

### Diagrama de flujo

![Diagrama de flujo](diagrama%20de%20flujo.jpg)

```txt
                                                          +----------------+
                                                          |     Inicio     |
                                                          +--------+-------+
                                                                   |
                                                                   v
                                                      +--------------------------+
                                                      | contenido, documentacion |
                                                      +--------------------------+
                                                                   |
                                                                   v
                                          +----------------------------------------------+
                                          | Abrir documentacion.md                       |
                                          | documentacion = documentacion.md             |
                                          | contenido = documentacion                    |
                                          +----------------------------------------------+
                                                                   |
                                                                   v
                                                      +------------------------+
 +--------------------------------------------------->| Mientras = True        |---NO------------------------+
 |                                                    +-----------+------------+                             |
 |                                                                | SI                                       |
 |                                                                v                                          |
 |    +-----------------------------------+   SI   +-------------------------------+                         |
 +----| contenido == "Documento de error" |<-------| caracteres de contenido > 0 ❓ |                        |
 |    +------------------+----------------+        +----------------+--------------+                         |
 |                                                                  | NO                                     |
 |                                                                  v                                        |
 |                                                 +---------------------------------+                       |
 |                                                 | titulos = extraer_subtitulos()  |                       |
 |                                                 +---------------------------------+                       |
 |                                                                |                                          |
 |     +----------------------------------+                       |                                          |
 |     | contenido = concatenar(contenido |  SI  +------------------------------------+                      |
 +-----| , "Documento de error")          |<-----| cantidad de items de titulos == 0❓ |                     |
 |     +----------------------------------+      +-------------------+----------------+                      |
 |                                                                | NO                                       |
 |                                                                v                                          |
 |                                      +-------------------------------------------------+                  |
 |                                      | mensaje, opciones = generar_opciones(titulos)   |                  |
 |                                      +-------------------------------------------------+                  |
 |                                                                |                                          |
 |                                                                v                                          |
 |                                         +--------------------------------------------+                    |
 |                                 +------>| opcion no existe o no está en opciones❓   |---NO--+            |
 |                                 |       +-----------------+--------------------------+       |            |
 |                                 |                              |SI                           |            |
 |                                 |                              v                             |            |
 |                                 |                    +--------------------+                  |            |
 |                                 |                    | IMPRIMIR mensaje   |                  |            |
 |                                 |                    +--------------------+                  |            |
 |                                 |                              |                             |            |
 |                                 |                              v                             |            |
 |                                 |                  +------------------------+                |            |
 |                                 +------------------| Ingresar opción        |                |            |
 |                                                    +-----------+------------+                |            |
 |                                                                                              |            |
 |                                                   inicio                                     |            |
 |     +---------------------------+            SI  +--------------------------+                |            |
 +-----| contenido = documentacion |<---------------| opción == opciones[-2]❓ |<---------------+            |
 |     +---------------------------+                +----------------+---------+                             |
 |                                                                 | NO                                      |
 |                                                     cerrar      v                                         V
 |                                                   +--------------------------+                       +--------+
 |                                                   | opción == opciones[-1]❓ |---------------------->|  Fin   |
 |                                                   +--------+-----------------+                       +--------+
 |                                                                 |NO
 |                                                                 v                       
 |                                        +-------------------------------------------------+
 |                                        | bloques = extraer_bloques(contenido)            |
 |                                        | bloque_elegido = bloques[opcion-1]              |
 |                                        | bloque_elegido_hijos = extraer_bloques(bloque)  |
 |                                        +--------------------+----------------------------+
 |                                                                  |
 |  +------------------------------+                                v
 |  | contenido = bloque_elegido   |       NO  +----------------------------------+
 |  | (para analizar subbloques)   |<----------| bloque_elegido_hijos no existe❓ |
 |  +------------------------------+           +----------------+-----------------+
 |                                                              | SI
 |                                                              v
 |                                                     +----------------+
 |                                                     | IMPRIMIR       |
 |                                                     | bloque_elegido |
 |                                                     +----------------+
 |                                                              |
 |                                                              v
 |                                          +---------------------------------------+
 |                                          | INGRESAR cualquier cosa               |
 +------------------------------------------| "Presionar enter para continuar..."   |
                                            +---------------------------------------+
```

## Sugerencias

> Nota: Como poseo conocimientos básicos en Python decidí usar ChatGPT para lidiar con dudas específicas.

Preguntas generales a ChatGPT:

- **¿Qué librería en python puedo usar para imprimir formato Markdown en consola?**
	- Resumen de respuestas: Rich con los objetos Consola y Markdown. Se instancia consola y se pasa el texto en formato `md` al objeto Markdown para ingresarlo a la instancia de Consola.
- **¿Cómo puedo separar texto Markdown por títulos del mismo nivel de header?**
	- Resumen de respuestas: Usar la librería `re` para aplicar regex al texto. Se debe usar `re.findall` para separar en bloques de texto según el patrón dado. Para que se pueda leer adecuadamente un Markdown que tiene saltos de línea y caracteres especiales, el patrón `.` debe leer todo y el patrón `^` considerar saltos de línea, así que usar: `flag=re.MULTILINE | re.DOTALL`.
- **¿Cómo puedo poner en un cuadrado o un marco un texto con rich?**
	- Resumen de respuestas: Con el objeto Panel.
- **¿Cómo dar color a un texto en Rich porque el objeto Panel elimina los estilos?**
	- Resumen de respuestas: Con `[estilo][/estilo]`. En estilo se puede escribir el color.

Como se puede ver, se hicieron preguntas específicas para solucionar vacíos de conocimiento en python sobre el estilo de impresión en consola y la separación de contenidos.

Se tuvieron que hacer varias preguntas para hacer entender a ChatGPT el resultado que quería lograr con regex, así que se sugiere invertir más tiempo en explicarle lo que se desea obtener. Se sugiere también pedir que explique el regex para poder corregir errores.
