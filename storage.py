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