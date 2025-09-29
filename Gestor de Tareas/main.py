from task_manager.manager import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\n--- TASK MANAGER ---")
        print("1. Listar tareas")
        print("2. Agregar tarea")
        print("3. Eliminar tarea")
        print("4. Cambiar estado")
        print("0. Salir")

        option = input("Seleccione una opción: ")

        if option == "1":
            manager.list_tasks()
        elif option == "2":
            title = input("Título: ")
            desc = input("Descripción: ")
            manager.add_task(title, desc)
        elif option == "3":
            task_id = int(input("ID de la tarea a eliminar: "))
            manager.delete_task(task_id)
        elif option == "4":
            task_id = int(input("ID de la tarea: "))
            task = next((t for t in manager.tasks if t.id == task_id), None)
            if task:
                task.toggle_status()
                manager.save_tasks()
        elif option == "0":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()