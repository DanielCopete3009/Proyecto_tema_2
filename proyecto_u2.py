import re #


# Definición de Colores ANSI

COLOR_RED = '\033[91m'
COLOR_GREEN = '\033[92m'
COLOR_YELLOW = '\033[93m'
COLOR_BLUE = '\033[94m'
COLOR_RESET = '\033[0m'
#Proyecto de programación tema 2
# Se pide crear un programa que gestione
# productos utilizando una matriz de datos y
# valide los nombres de los productos utilizando expresiones regulares.


# Matriz e Inicialización
# La matriz (lista de listas) se inicializa con 5 productos.
# Cada sub-lista tiene 3 campos: [ID, Nombre, Stock]

def inicializar_inventario():
    """
    Crea y devuelve la matriz de inventario inicial
    """
#     Los nombres han sido ajustados para CUMPLIR las reglas
#     de validación

    Inventario = [
        [101,"MonitorAOC24",25],
        [102,"TecladoK120",20],
        [103,"MandoPro4",30],
        [104,"MouseGamerG502",15],
        [105,"WebcamC920",35]
    ]
    
    print(f"{COLOR_BLUE}Inventario inicializado con {len(Inventario)} productos.{COLOR_RESET}")
    return (Inventario)


#Busqueda y manejo de errores


def buscar_producto_por_id(inventario):
    """
    Pide un id al usuario y busca el producto en la matriz.
    Muestra los detalles si lo encuentra o un error en rojo
    si no lo ha encontrado
    """
    print(f"\n{COLOR_BLUE}--- Búsqueda de Producto por ID ---{COLOR_RESET}")
    try:
        #Pedimos el ID y lo convertimos a entero
        id_buscar_str = input(f"{COLOR_YELLOW}Introduce el ID del producto a buscar: {COLOR_RESET}")
        id_buscar = int(id_buscar_str)
    except ValueError:
        print(f"{COLOR_RED}Error: El ID debe ser un número entero.{COLOR_RESET}")
        return
    
    
    encontrado=False
    #Recorremos la matriz
    for producto in inventario:
        if producto [0] == id_buscar:
            print(f"{COLOR_GREEN}Producto encontrado:{COLOR_RESET}")
            print(f"	Nombre: {producto[1]}")#Producto[1] es el nombre
            print(f"	Stock: {producto[2]}")#Producto[2] es el stock
            encontrado = True
            break#el id es único, podemos detener la búsqueda
        
    if not encontrado:
        print(f"{COLOR_RED}Error: Producto con ID {id_buscar} no encontrado.{COLOR_RESET}")
        
#Operación de Comparación
def comparar_stock(inventario):
    """
    Recorre la matriz para enconrtrar el producto con más y menos stock.
    Imprime los nombres de ambos productos.
    """
    
    print(f"\n{COLOR_BLUE}--- Comparación de Stock (Máx/Mín) ---{COLOR_RESET}")
    
    if not inventario:
        print(f"{COLOR_RED}El inventario está vacío. No se puede comparar.{COLOR_RESET}")
        return
    
    #Asumimos que el primer producto es el max y min para empezar a comparar
    producto_max_stock = inventario[0]
    producto_min_stock = inventario[0]
    
    #Recorremos la matriz
    for producto in inventario:
        #producto[2] es la columna del Stock
        #Comparamos para encontrar el máximo
        if producto[2] > producto_max_stock[2]:
            producto_max_stock = producto
            
        #Comparar para encontrar el mínimo
        if producto[2] < producto_min_stock[2]:
            producto_min_stock = producto
            
    #Imprimimos los NOMBRES de los productos, como pide la rúbrica
    print(f"Producto con MÁS stock: {COLOR_GREEN}{producto_max_stock[1]}{COLOR_RESET} (Stock: {producto_max_stock[2]})")
    print(f"Producto con MENOS stock: {COLOR_RED}{producto_min_stock[1]}{COLOR_RESET} (Stock: {producto_min_stock[2]})")

# Implementación RegEx
def validar_nuevo_producto():
    """
    Pide un nombre de producto y lo valida usando Expresiones Regulares.
    Debe cumplir 3 criterios: Mayúscula inicial, al menos un dígito, y longitud.
    Imprime el resultado en VERDE o ROJO con la razón del fallo.
    """
    print(f"\n{COLOR_BLUE}--- Validación de Nombre de Producto ---{COLOR_RESET}")
    nombre = input(f"{COLOR_YELLOW}Introduce el nombre del nuevo producto a validar: {COLOR_RESET}")
    
    errores = [] #Esto es un recopilador de errores, los errores que se hayan encontrado en "validar_nuevo_producto" se recopilaran aqui

    # 1. Regla: Longitud total entre 5 y 20 caracteres
    if not (5 <= len(nombre) <= 20):
        errores.append(f"Longitud inválida (debe ser entre 5-20 caracteres, tiene {len(nombre)}).")

    # 2. Regla: Debe empezar con una letra mayúscula (A-Z)
    # ^[A-Z] -> ^ (ancla al inicio) [A-Z] (una letra mayúscula)
    if not re.search(r'^[A-Z]', nombre): #r lo que hace es que python interprete este caracter de escape, indicando que es un raw string, asi evitamos las \
        errores.append("Debe empezar con una letra mayúscula.")

    # 3. Regla: Debe contener al menos un dígito (0-9)
    # \d -> Busca cualquier dígito en cualquier parte de la cadena
    if not re.search(r'\d', nombre):
        errores.append("Debe contener al menos un dígito.")

    # Reporte de resultados
    if not errores:
        # Requisito: Mensaje de éxito en VERDE
        print(f"{COLOR_GREEN}Éxito: El nombre '{nombre}' es VÁLIDO.{COLOR_RESET}")
    else:
        # Requisito: Mensaje de error en ROJO con razones
        print(f"{COLOR_RED}Error: El nombre '{nombre}' es INVÁLIDO:{COLOR_RESET}")
        for error in errores:
            print(f"{COLOR_RED}  - {error}{COLOR_RESET}")

# Claridad y Presentación (Menú Principal)
def main():
    """
    Función principal que organiza el programa en un menú interactivo.
    """
    inventario = inicializar_inventario()

    while True:
        print("\n" + "="*40)
        print(f"{COLOR_BLUE}   Sistema de Gestión de Productos   {COLOR_RESET}")
        print("="*40)
        print("1. Buscar producto por ID")
        print("2. Comparar stock (Max/Min)")
        print("3. Validar nombre de nuevo producto")
        print("4. Salir")
        print("="*40)
        
        opcion = input(f"{COLOR_YELLOW}Seleccione una opción (1-4): {COLOR_RESET}")

        if opcion == '1':
            buscar_producto_por_id(inventario)
        elif opcion == '2':
            comparar_stock(inventario)
        elif opcion == '3':
            validar_nuevo_producto()
        elif opcion == '4':
            print(f"{COLOR_BLUE}Saliendo del sistema...{COLOR_RESET}")
            break
        else:
            print(f"{COLOR_RED}Opción no válida. Por favor, intente de nuevo.{COLOR_RESET}")

# Punto de entrada del script
if __name__ == "__main__": #Esta es una línea estándar en Python. Simplemente significa "cuando ejecute este archivo .py, empieza por llamar a la función
    main()


