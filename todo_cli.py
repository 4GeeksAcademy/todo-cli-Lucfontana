import csv

tasks = []

def menu():
    print("---TODO CLI - ELIGE UNA OPCIÓN---")
    print(f"""
    1- Añadir una tarea
    2- Mostrar lista de tareas
    3- Eliminar tarea
    4- Exportar tareas a .csv
    5- Cargar tareas desde .csv
    6- Salir
    """)

def add_one_task(name):
    global tasks
    clean_name = name.strip()
    if not clean_name:
        print("El nombre de la tarea no puede estar vacío")
        return

    tasks.append(clean_name)
    print("Tarea añadida exitosamente")
    print_list()

def print_list():
    global tasks

    if not tasks:
        print("No hay tareas todavía")
        return

    for i in range(len(tasks)):
        print(f"Tarea número {i}: {tasks[i]}")


def delete_task(index):
    global tasks

            # Forma segura de verificar tipos (acepta herencia tambien)
    if not isinstance(index, int):
        print("Ingrese un número")
        return

    if index < 0:
        print("El índice no puede ser negativo")
        return

    if index < len(tasks):
        tasks.pop(index)
        print("Tarea eliminada exitosamente")
    else:
        print("El index seleccionado no existe")


def export_tasks_to_csv(file_name):
    global tasks

    with open(file_name, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["task"])
        for task in tasks:
            writer.writerow([task])

    print(f"Tareas exportadas correctamente a {file_name}")


def load_tasks_from_csv(file_name):
    global tasks

    with open(file_name, mode="r", newline="", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        rows = list(reader)

    if not rows:
        tasks = []
        print("Archivo vacío. No se cargaron tareas")
        return

    start_index = 1 if rows[0] and rows[0][0].strip().lower() == "task" else 0
    loaded_tasks = []

    for row in rows[start_index:]:
        if row:
            task_name = row[0].strip()
            if task_name:
                loaded_tasks.append(task_name)

    if tasks:
        print("Ya hay tareas cargadas en memoria")
        print("1- Combinar listas")
        print("2- Priorizar archivo (reemplazar lista actual)")
        print("3- Cancelar")

        while True:
            action = input("Elige una opción (1, 2 o 3): ").strip()

            if action == "1":
                tasks.extend(loaded_tasks)
                print(
                    f"Se combinaron listas. Total actual: {len(tasks)} tareas"
                )
                break
            if action == "2":
                tasks = loaded_tasks
                print(f"Se cargaron {len(tasks)} tareas desde {file_name}")
                break
            if action == "3":
                print("Carga de tareas cancelada")
                break

            print("Opción inválida. Ingresa 1, 2 o 3")
    else:
        tasks = loaded_tasks
        print(f"Se cargaron {len(tasks)} tareas desde {file_name}")


while True:
    menu()

    opc = input("\nSelecciona una opción:")

    if opc == "1":
        nombre_task = input("Escribe el nombre de la tarea: ")
        add_one_task(nombre_task)
    elif opc == "2":
        print_list()
    elif opc == "3":
        index_text = input("Ingrese el índice de la tarea a eliminar: ")
        if index_text.isdigit() or (index_text.startswith("-") and index_text[1:].isdigit()):
            delete_task(int(index_text))
        else:
            print("Ingrese un índice válido")
    elif opc == "4":
        file_name = input("Nombre del archivo CSV (enter para usar tasks.csv): ").strip()
        if not file_name:
            file_name = "tasks.csv"
        try:
            export_tasks_to_csv(file_name)
        except OSError as err:
            print(f"No se pudo exportar el archivo: {err}")
    elif opc == "5":
        file_name = input("Nombre del archivo CSV a cargar (enter para usar tasks.csv): ").strip()
        if not file_name:
            file_name = "tasks.csv"
        try:
            load_tasks_from_csv(file_name)
        except FileNotFoundError:
            print("El archivo indicado no existe")
        except OSError as err:
            print(f"No se pudo cargar el archivo: {err}")
    elif opc == "6":
        break
    else:
        print("Opción inválida")
        continue




