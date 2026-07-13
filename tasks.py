from storage import guardar_tareas

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
     tarea_agregada = input("¿Qué tarea quieres agregar? ")
     tarea_agregada = tarea_agregada.strip()
     while True :
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
            break