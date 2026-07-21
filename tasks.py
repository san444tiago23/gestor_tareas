from storage import guardar_tareas
from filters import filtrar, combinar_and, negar

def mostrar_tareas(lista):
        contador = 0
        for i in lista:
            contador += 1
            if i["completada"]:
                simbolo = "✔"
            else:
                simbolo = "❌"
            print(contador, i["nombre"], simbolo)

def tarea_noregistrada(lista):
    if not lista:
            print("No hay tareas registradas")
            return True
    return False

def pedir_indice(mensaje):
    entrada = input(mensaje)
    entrada = entrada.strip()

    if not entrada.isdigit():
        print("Por favor ingresa un número válido")
        return None
    return int(entrada)

def agregar_tarea(nueva_tarea):
     while True :
        tarea_agregada = input("¿Qué tarea quieres agregar? ")
        tarea_agregada = tarea_agregada.strip()
        if tarea_agregada == "" :
            print("Por favor ingresa una tarea valida")
        else:
            nueva_tarea.append({
            "nombre": tarea_agregada,
            "completada": False
            })
            guardar_tareas(nueva_tarea)
            print(f"Tarea '{tarea_agregada}' agregada exitosamente.")
            print("Ahora tienes" , len(nueva_tarea) , "tareas agregadas")
            return

def marcar_tarea_completada(nueva_tarea):
    while True:
        if tarea_noregistrada(nueva_tarea):
            return
        mostrar_tareas(nueva_tarea)
        indice = pedir_indice("¿Qué tarea completaste? ")
        if indice is None:
            continue
        numero_indice = indice - 1
        if indice < 1 or indice > len(nueva_tarea): #valida que el indice este dentro del rango de la lista de tareas
            print("Ese indice no existe")
            continue
        else:
            if nueva_tarea[numero_indice]["completada"]: # valida que la tarea ya este completada
                print("Esta tarea ya esta completa")
                continue
            else:
                tarea_completada = nueva_tarea[numero_indice]["nombre"]
                nueva_tarea[numero_indice]["completada"] = True
                guardar_tareas(nueva_tarea) 
                print(f"Tarea" , tarea_completada  ,"completada")
                mostrar_tareas(nueva_tarea)
                return

def eliminar_tarea(nueva_tarea):
    while True:
        if tarea_noregistrada(nueva_tarea):
            return
        mostrar_tareas(nueva_tarea)
        indice = pedir_indice("¿Qué tarea deseas eliminar? ")
        if indice is None:
            continue
        numero_indice = indice - 1
        if indice < 1 or indice > len(nueva_tarea):
            print(f"Esa tarea no se puede eliminar")
            continue    
        else:
            nueva_tarea.pop(numero_indice)
            guardar_tareas(nueva_tarea)
            print(f"Tarea" , (numero_indice + 1),"eliminada")
            mostrar_tareas(nueva_tarea)
            return

def ver_tareas_por_estado(nueva_tarea, estado):
        if tarea_noregistrada(nueva_tarea):
            return
        lista_filtrada = filtrar(nueva_tarea, lambda t: t ["completada"] == estado)
        return lista_filtrada

def ver_tarea_por_nombre(nueva_tarea):
    while True:
        if tarea_noregistrada(nueva_tarea):
            return
        nombre_filtrado = input("¿Que tarea deseas filtrar? ")
        nombre_filtrado = nombre_filtrado.strip()
        if not nombre_filtrado:
            print(f'Por favor escribir un nombre valido')
            continue
                #lista_connombre = filtrar_nombre(nueva_tarea, nombre_filtrado)
        nombre_filtrado = nombre_filtrado.lower()
        #condicion_completadas = lambda t: t.get ["completada"] == estado
        condicion_nombre = lambda t: nombre_filtrado in t.get("nombre", "").lower()
        #condicion_final = combinar_and(negar(condicion_completadas), condicion_nombre)
        resultado = filtrar(nueva_tarea, condicion_nombre)
        if not resultado:
            print("Esa tarea no esta en nuestra lista")
        else:
            mostrar_tareas(resultado)
            return
        
def editar_tarea(nueva_tarea):
    while True:
        if tarea_noregistrada(nueva_tarea):
            return
        nombre_filtrado = input("¿Que tarea deseas filtrar? ")
        nombre_filtrado = nombre_filtrado.strip()
        if not nombre_filtrado:
            print(f'Por favor escribir un nombre valido')
            continue
        nombre_filtrado = nombre_filtrado.lower()
        condicion_nombre = lambda t: nombre_filtrado in t.get("nombre", "").lower()
        resultado = filtrar(nueva_tarea, condicion_nombre)
        if not resultado:
            print("Esa tarea no esta en nuestra lista")
            continue
        else:
            while True:
                mostrar_tareas(resultado)
                indice = pedir_indice("Que tarea deseas editar? ")
                if indice is None:
                    continue
                if indice < 1 or indice > len(resultado):
                    print("Índice fuera de rango")
                    continue
                numero_indice = indice - 1
                tarea_seleccionada = resultado[numero_indice]
                #while True:
                entrada = (input("¿Que desea editar? " f"1. Editar nombre " f"2. Editar estado "))
                entrada = entrada.strip()
                if not entrada.isdigit():
                    print(f"Por favor ingresa un número válido")
                    continue
                else:
                    opcion = int(entrada)
                    if opcion not in (1, 2):
                        print("Esa opción no es correcta")
                        continue
                    se_edito = False
                    while True:
                        if opcion == 1:
                            nuevo_nombre = input("Escriba el nuevo nombre: ").strip()
                            if not nuevo_nombre:
                                print("Nombre inválido")
                                continue
                            tarea_seleccionada["nombre"] = nuevo_nombre
                            se_edito = True
                        elif opcion == 2:
                            estado = input("Nuevo estado (1 completada / 0 pendiente): ").strip()
                            if estado == "1":
                                if tarea_seleccionada["completada"]:
                                    print("Esa tarea ya esta completada")
                                    return
                                else:
                                    tarea_seleccionada["completada"] = True
                                    se_edito = True
                            elif estado == "0":
                                if not tarea_seleccionada["completada"]:
                                    print("La tarea ya está pendiente")
                                    return
                                else:
                                    tarea_seleccionada["completada"] = False
                                    se_edito = True
                            else:
                                print("Valor inválido")
                                continue
                        if se_edito:
                            guardar_tareas(nueva_tarea)
                            print("Tarea actualizada correctamente")
                        mostrar_tareas(resultado)
                        return

#editar_tarea() terminó siendo demasiado grande. En una versión futura la dividiría en funciones más pequeñas (buscar_tareas_por_nombre, seleccionar_tarea, editar_nombre, editar_estado)