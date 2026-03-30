from servicios import * # Importa todas las funciones del modulo servicios
menu_mensaje_1() #Imprime por consola el mensaje de bienvenida




def loop(): #Funcion loop que ejecuta el programa una y otra vez hasta que el usuario decida salir
    """
    5) funcion que inicia el programa que posterios se puede cerrar cuando el usuario decida salir cambiando el valor 
    de la variable.
    """
    loop_var = 0
    while loop_var != 6:
        menu_interactivo()
        loop_var = options()

def options(): #Funcion que interactua con las demas funciones del modulo servicio ejecuntado de forma secuencial el codigo

    """
    Esta funcion es la encarga de orquestar todo el progrma, con validacion optimas que permiten el flujo ordenado del sistema, cada opcion llama a un 
    funcion en particualar, luego de que dicha funcion se cumpla vuelve a iniciar el ciclo y asi susecivamente.
    """ 
    valid_option = False
    while not valid_option:
        try:
            option = int(input("\n>> Select an option: "))
            if 1 <= option <= 6:
                valid_option = True
            else:
                print("\nInvalid selection, enter a value between 1 and 6.")
        except ValueError:
            print("\nInvalid input. Please enter numbers only.")

    if option == 1:
        estudiante = registrar() #Llama a la funcion de registrar
        base.append(estudiante) #Almacena los datos del estudiante en la base 
        
    elif option == 2:
        print("="*35)
        for ls in base:
            print(f"| Nombre: {ls["Nombre"]} | ID: {ls["ID"]} | Edad: {ls["Edad"]} | Curso: {ls["Curso"]} | Estado: {ls["Estado"]}")
            #Imprime toda la informacion de la base de datos de cada estudiante
        print("="*35)

    elif option == 3:
        buscar_esutidante() #llama a la funcion nombrada

    elif option == 4:
        actualziar_datos() #llama a la funcion nombrada

    elif option == 5:
        eliminar() #llama a la funcion nombrada
    elif option == 6:
        print("Saliendo del sistema")
        exit()
    else:
        print("Selecione una opcion valida")
        return loop()



