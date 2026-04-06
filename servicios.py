base = [{"Nombre": "Daniel", "ID": 1111, "Edad": 22, "Curso": "RIWI", "Estado": "Activo"}]
# Lista que almacena diccionarios con la informacion de los estudiantes(Es la base de datos)

def menu_mensaje_1():
    print("="*35)
    print("BIENVENIDO AL SISTEMA")
    
#Mensaje de bienvenida

def menu_interactivo():
    print("="*35)
    print ("1. Registrar estudiante")
    print("2. Consultar lista de estudiante")
    print("3. Buscar estudiante")
    print("4. Actualizar informacion de un estudainte")
    print("5. Eliminar estudiante")
    print("6. Salir")
#Menu interactivo (Imprime en consola las opcines del menu)

    

def registrar(): #Funcion de registar un nuevo estudiante
        """
        1) registrar() es la funcion encargada de pedirle al usuario los datos del estudiante, que psoterios 
        sera almacena en la base de datos del programa, permitiendo un flujo adecuado. Cada informacion del estudiante sera almacenda 
        como un diccionario.
        """
        try: 
            nombre = input("\n| Ingrese el nombre del estudiante: ").strip().capitalize()
            id = int(input("| Ingrese el ID del estudiante: "))
            edad = int(input("| Ingrese la edad del estudiante: "))
            curso = input("| Ingrese el curso donde esta el estudainte: ").strip().capitalize()
            estado = input("| Ingrese el estado en el que se encuentra el estudiante: ").strip().capitalize()
            print("\n")
            datos_estudiante = ({"Nombre":nombre, "ID": id, "Edad": edad, "Curso": curso, "Estado": estado})
            # Retorna el diccionario con los datos del estudiante
            return datos_estudiante
        except ValueError:
            print("="*35)
            print ("Valor errado, vuelva intentarlo")
            return registrar
    
def buscar_esutidante(): #Funcion para buscar la informacion del estudiante en particular
    """ 
    2) buscar_estudiante() como su nombre lo indica es la funcion que permite buscar
    por ID del estudiante para proporcionar los datos de un solo estudiante y no tener que buscarlo en 
    la base de datos.
    """
    validar = 0
    while validar != 1:
        try:
            buscar = int(input("\n| Ingrese el ID del estudiante: "))
        
            for ls in base:
                if ls["ID"] == buscar:
                    registro = True
                    Estudiante = (f"| Nombre: {ls["Nombre"]} | ID: {ls["ID"]} | Edad: {ls["Edad"]} | Curso: {ls["Curso"]} | Estado: {ls["Estado"]}")
                    print("="*35)
                    print (Estudiante)
                    print("="*35)
                    
                    
                    buscar_otro = input(">> Desea buscar otro estudiante? (Y/N): ").upper()
                    # Condicion que nos permite buscar otro estudiante si el usuario lo requiere
                    if buscar == "Y":
                        return buscar_esutidante
                    else:
                        validar = 1     
                else:
                    print("="*35)
                    print("| El estudiante no esta registrado")
                    validar = 1   
                
        except ValueError:
            print ("| Dato errado, vuelva a intentarlo")
            
            return Estudiante


def actualziar_datos(): #Funcion encarga de actualizar datos puntual del estudiante
    """
    3) Esta funcion cumple con la carecteristca de actulizar los datos de un solo estudiante a la vez, primero se busca el id del estudiante
    luego el sistema valida si esta en la base datos, si esta continua con el proceso pidiendole al usario que dato como tal quiere actulizar, si el estudiante
    no esta en la base de datos o dado caso hubo un erro al digitar el id el sistema lanza un mensaje de error retornado al menu.
    """


    validar = 0
    while validar != 1:
        try:
            buscar = int(input("\n| Ingrese el ID del estudiante: "))
            for ls in base:
                if ls["ID"] == buscar:
                    registro = True
                    print("="*35)
                    print(f"| Nombre: {ls["Nombre"]} | ID: {ls["ID"]} | Edad: {ls["Edad"]} | Curso: {ls["Curso"]} | Estado: {ls["Estado"]}")
                    print("="*35)
                    print("Que desea actualizar?")
                    print("1.Nombre")
                    print("2.Edad")
                    print("3.Curso")
                    print("4.Estado")

                    valid_sub = False
                    while not valid_sub:
                        try:
                            actualizar = int(input(">> Select an option: "))
                            if 1 <= actualizar <= 4:
                                valid_sub = True
                            else:
                                print("Invalid option, enter 1, 2, 3 or 4.")
                        except ValueError:
                            print("Invalid input. Enter a number.")

                        #Actualiza las variables por unas nuevas, que seran alojadas en la base de datos
                            if actualizar == 1:
                                new_name = input(" Nuevo nombre: ").capitalize().strip()
                                ls["Name"] = new_name

                            elif actualizar == 2:
                                new_edad = int(input("| Nuevo edad: "))
                                ls["Edad"] = new_edad

                            elif actualizar == 3:
                                new_curso = int(input("| Nuevo curso: "))
                                ls["Curso"] = new_curso

                            elif actualizar == 4:
                                new_estado =input("| Nuevo estado")
                                ls["Estado"] = new_estado

                            print ("| Estudiante actualizado")
                            break
                else:
                    print("="*35)
                    print("| El estudiante no esta registrado")
                    validar = 1  

            
        except ValueError:
            print ("| Dato errado, vuelva a intentarlo")

def eliminar(): #Funcion de eliminar toda la informacion de un estudiante
    """
    4) Esta funcion cumple con el criterio de eliminar de la base de datos toda la informacion del estudiante, primero se ahce una validacion,
    si ingresa el id del estudiante y posterios se ejecuta un mensaje para confirmar si de verdad quiere eliminar al estudiante lo que ejecuta la condicion 
    de eliminar al estudiante de la base de datos, y sino es le caso, el progrma vuelve al menu de inicio.
    """
    buscar = int(input(">> Ingrese el ID del estudiante: "))
    
    for ls in base:
        if buscar == ls["ID"]:
            confirmacion = input(f">> Seguro que desea eliminar al estudiante con el ID: {buscar}: Y/N?: ").upper()
            if confirmacion == "Y":
                for ls in base:
                    ls["ID"] 
                    base.remove(ls)
                    print("\n>> Estudiante eliminado")
            else:
                print("\n>> Accion cancelada")
        else:
            print("\n>> Estudiante no encontrado")
            
    
    
    