
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
	13. **Sino-Si** `opcion` == `opciones[-2]`
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
