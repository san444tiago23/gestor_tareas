# Proyecto gestor de tareas

from storage import guardar_tareas, cargar_tareas
from tasks import mostrar_tareas, tarea_noregistrada, pedir_indice, agregar_tarea, eliminar_tarea, marcar_tarea_completada, ver_tareas_por_estado, ver_tarea_por_nombre, editar_tarea
from filters import filtrar, combinar_and, combinar_or, negar

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



nueva_tarea = cargar_tareas()
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
        agregar_tarea(nueva_tarea)
    elif tarea == "2":
        if tarea_noregistrada(nueva_tarea):
            continue
        mostrar_tareas(nueva_tarea)
    elif tarea == "3":
        marcar_tarea_completada(nueva_tarea)
    elif tarea == "4":
        eliminar_tarea(nueva_tarea)  
    elif tarea == "5":
        resultado = ver_tareas_por_estado(nueva_tarea, False)
        if not resultado:
            print("No quedan tareas pendientes")
        else:
            mostrar_tareas(resultado)
    elif tarea == "6":
        
        resultado = ver_tareas_por_estado(nueva_tarea, True)
        if not resultado:
            print("No quedan tareas completadas")
        else:
            mostrar_tareas(resultado)
    elif tarea == "7":
        ver_tarea_por_nombre(nueva_tarea)
        '''if tarea_noregistrada(nueva_tarea):
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
                mostrar_tareas(resultado)'''
    elif tarea == "8":
        editar_tarea(nueva_tarea)
        '''if tarea_noregistrada(nueva_tarea):
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
                indice = pedir_indice("Que tarea deseas editar? ")
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
                    mostrar_tareas(resultado)'''
                    # Primera modificación después del commit
