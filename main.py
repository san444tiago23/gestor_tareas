# Proyecto gestor de tareas

import json
def guardar_tareas(lista):
    with open("tareas.json", "w") as archivo:
        json.dump(lista, archivo)

def cargar_tareas():
    try:
        with open("tareas.json", "r") as archivo:
            datos = json.load(archivo)
            nueva_lista = []
            for i in datos:
                if type(i) == str:
                    if "✔" in i:
                        completada = True
                        nombre = i.replace(" ✔" , "")
                        nueva_lista.append({
                        "nombre": nombre,
                        "completada": completada
                        })
                    elif "✔" not in i:
                        completada = False
                        nombre = i
                        nueva_lista.append({
                        "nombre": nombre,
                        "completada": completada
                        })
                else:
                    nueva_lista.append(i)
            return nueva_lista
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    
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

'''def filtrar_tareas(lista, estado):
        lista_filtrada = []
        for i in lista:
            if i["completada"] == estado:
                lista_filtrada.append(i)
        return lista_filtrada
def filtrar_nombre(lista, nombres):
        lista_connombre = []
        for i in lista:
            nombre = i.get("nombre")
            if nombre is not None:
                if nombres.lower() in nombre.lower():
                    lista_connombre.append(i)
        return lista_connombre'''

def pedir_indice(mensaje):
    entrada = input(mensaje)
    entrada = entrada.strip()

    if not entrada.isdigit():
        print("Por favor ingresa un número válido")
        return None
    return int(entrada)

def filtrar(lista, condicion):
    lista_filtrada = []
    for i in lista:
        if condicion(i):
            lista_filtrada.append(i)
    return lista_filtrada

def combinar_and(c1, c2):
    return lambda t: c1(t) and c2(t)

def combinar_or(c1, c2):
    return lambda t: c1(t) or c2(t)

def negar(c):
    return lambda t: not c(t)

nueva_tarea = cargar_tareas()
print(cargar_tareas())

while True:
    print("Gestor de tareas")
    print("1. Agrerar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Ver tareas pendientes")
    print("6. Ver tareas completadas")
    print("7. Filtrar tarea por nombre")
    print("8. Editar tarea")
    
    tarea = input("¿Qué tarea quieres realizar? ")
    if not tarea.isdigit(): #valida que sea un numero y no letras
            print(f"Por favor ingresa un número válido")
            continue
    else:
        print(f"Has seleccionado la tarea: {tarea}")


    if tarea == "1": 
        tarea_agregada = input("¿Qué tarea quieres agregar? ")
        nueva_tarea.append({
        "nombre": tarea_agregada,
        "completada": False
        })
        guardar_tareas(nueva_tarea)
        print(f"Tarea '{tarea_agregada}' agregada exitosamente.")
        print("Ahora tienes" , len(nueva_tarea) , "tareas agregadas")
    elif tarea == "2":
        if tarea_noregistrada(nueva_tarea):
            continue
        mostrar_tareas(nueva_tarea)
    elif tarea == "3":
        if tarea_noregistrada(nueva_tarea):
            continue
        mostrar_tareas(nueva_tarea)
        indice = pedir_indice("¿Qué tarea completaste? ")
        if indice is None:
            continue
        numero_indice = indice - 1
        if indice < 1 or indice > len(nueva_tarea): #valida que el indice este dentro del rango de la lista de tareas
            print("Esa tarea no esta agregada")
        else:
            if nueva_tarea[numero_indice]["completada"]: # valida que la tarea ya este completada
                print("Esta tarea ya esta completa")
            else:
                tarea_completada = nueva_tarea[numero_indice]["nombre"]
                nueva_tarea[numero_indice]["completada"] = True
                guardar_tareas(nueva_tarea) 
                print(f"Tarea" , tarea_completada  ,"completada")
                mostrar_tareas(nueva_tarea)
    elif tarea == "4":
        if tarea_noregistrada(nueva_tarea):
            continue
        mostrar_tareas(nueva_tarea)
        entrada = (input("Que tarea deseas eliminar? "))
        entrada = entrada.strip()
        if not entrada.isdigit():
            print(f"Por favor ingresa un número válido")
        else:
            indice = int(entrada)
            if indice < 1 or indice > len(nueva_tarea):
                print("Esa tarea no se puede eliminar")
            else:
                numero_indice = indice - 1
                nueva_tarea.pop(numero_indice)
                guardar_tareas(nueva_tarea)
                print(f"Tarea" , (numero_indice + 1),"eliminada")
                mostrar_tareas(nueva_tarea)    
    elif tarea == "5":
        if tarea_noregistrada(nueva_tarea):
            continue
            #lista_filtrada_pendientes = filtrar_tareas(nueva_tarea, False)
        lista_filtrada_pendientes = filtrar(nueva_tarea, lambda t: t["completada"] == False)
        if not lista_filtrada_pendientes:
            print("No quedan tareas pendientes por realizar")
        else:
            mostrar_tareas(lista_filtrada_pendientes)
    elif tarea == "6":
        if tarea_noregistrada(nueva_tarea):
            continue
            #lista_filtrada = filtrar_tareas(nueva_tarea, True)
        lista_filtrada = filtrar(nueva_tarea, lambda t: t["completada"] == True)
        if not lista_filtrada:
            print("No hay tareas completadas")
        else:
            mostrar_tareas(lista_filtrada)
    elif tarea == "7":
        if tarea_noregistrada(nueva_tarea):
            continue
        nombre_filtrado = input("¿Que tarea deseas filtrar? ")
        nombre_filtrado = nombre_filtrado.strip()
        if not nombre_filtrado:
            print(f'Por favor escribir un nombre valido')
        else:
                #lista_connombre = filtrar_nombre(nueva_tarea, nombre_filtrado)
            nombre_filtrado = nombre_filtrado.lower()
            condicion_completadas = lambda t: t.get("completada", False)
            condicion_nombre = lambda t: nombre_filtrado in t.get("nombre", "").lower()
            condicion_final = combinar_and(negar(condicion_completadas), condicion_nombre)
            resultado = filtrar(nueva_tarea, condicion_final)
            if not resultado:
                print("Esa tarea no esta en nuestra lista")
            else:
                mostrar_tareas(resultado)
    elif tarea == "8":
        if tarea_noregistrada(nueva_tarea):
            continue
        nombre_filtrado = input("¿Que tarea deseas filtrar? ")
        nombre_filtrado = nombre_filtrado.strip()
        if not nombre_filtrado:
            print(f'Por favor escribir un nombre valido')
            continue
        else:
            nombre_filtrado = nombre_filtrado.lower()
            condicion_nombre = lambda t: nombre_filtrado in t.get("nombre", "").lower()
            resultado = filtrar(nueva_tarea, condicion_nombre)
            if not resultado:
                print("Esa tarea no esta en nuestra lista")
                continue
            else:
                mostrar_tareas(resultado)
                indice = pedir_indice = (input("Que tarea deseas editar? "))
                if indice < 1 or indice > len(resultado):
                    print("Índice fuera de rango")
                    continue
                numero_indice = indice - 1
                tarea_seleccionada = resultado[numero_indice]
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
                            else:
                                tarea_seleccionada["completada"] = True
                                se_edito = True
                        elif estado == "0":
                            if not tarea_seleccionada["completada"]:
                                print("La tarea ya está pendiente")
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
                    # Primera modificación después del commit
                        

                        

        
