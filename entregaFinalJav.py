# =====================================================================================================
#                                SISTEMA DE GESTIÓN DE PRODUCTOS
# Autor: Julio Alejandro Vázquez.
# Comisión #26207
# =====================================================================================================


# Creo la lista stock, que contiene todos los productos.
# Cada producto es otra lista con estos datos:
# [identificador, nombre, categoria, descripcion, cantidad, precio]
stock = [
    ["1", "Notebook", "Tecnologia", "Computadora personal", 600, 850000],
    ["2", "Mouse", "Perifericos", "Dispositivo apuntador para computadora", 35, 25000],
    ["3", "Teclado", "Perifericos", "Dispositivo de entrada de texto", 20, 45000],
    ["4", "Monitor", "Tecnologia", "Pantalla para computadora", 15, 320000],
    ["5", "Auriculares", "Audio", "Dispositivo para escuchar sonido", 42, 75000],
    ["6", "Webcam", "Perifericos", "Camara para videollamadas", 18, 60000],
    ["7", "Parlantes", "Audio", "Altavoces para reproducir sonido", 27, 55000],
    ["8", "Impresora", "Oficina", "Equipo para imprimir documentos", 9, 180000],
    ["9", "Tablet", "Tecnologia", "Dispositivo portatil con pantalla tactil", 31, 280000],
    ["10", "Pendrive", "Almacenamiento", "Memoria portatil USB", 55, 12000],
    ["11", "Disco SSD", "Almacenamiento", "Unidad de almacenamiento de estado solido", 24, 95000],
    ["12", "Router", "Redes", "Dispositivo para conectar equipos a una red", 13, 70000],
    ["13", "Mouse", "Perifericos", "Mouse basico para computadora", 48, 5000]
]


# Defino una funcion que recibe los datos de un producto
# y muestra cada uno de ellos en pantalla.
def mostrar_ficha(codigo, nombre_producto, rubro, detalle, unidades, valor):
    print("ID:", codigo)                  # Muestro el identificador del producto.
    print("Nombre:", nombre_producto)     # Muestro el nombre del producto.
    print("Categoria:", rubro)            # Muestro la categoria a la que pertenece.
    print("Descripcion:", detalle)        # Muestro la descripcion del producto.
    print("Cantidad:", unidades)          # Muestro la cantidad disponible.
    print("Precio:", valor)               # Muestro el precio del producto.
    print("")                             # Dejo una linea en blanco para separar productos.


# Defino una funcion para solicitar un dato al usuario.
# El parametro etiqueta indica que dato se esta solicitando.
def solicitar_dato(etiqueta):
    # Pido el dato, elimino espacios al principio y al final,
    # y convierto la primera letra de cada palabra a mayuscula.
    dato_ingresado = input(f"{etiqueta}: ").strip().title()

    # Mientras el usuario no ingrese ningun dato, vuelvo a solicitarlo.
    while dato_ingresado == "":
        print(f"{etiqueta} no puede estar vacio")

        # Vuelvo a pedir el dato y aplico las mismas transformaciones.
        dato_ingresado = input(f"{etiqueta}: ").strip().title()

    # Devuelvo el dato ingresado para poder utilizarlo fuera de la funcion.
    return dato_ingresado


# Creo la variable seleccion vacia para que el while pueda comenzar.
seleccion = ""


# Mientras la opcion elegida sea distinta de 7, el menu se seguira mostrando.
while seleccion != "7":

    # Muestro por pantalla las opciones disponibles del sistema.
    print("""
    1. Agregar producto
    2. Mostrar productos
    3. Buscar producto
    4. Actualizar producto
    5. Eliminar producto
    6. Reporte de stock
    7. Salir
    """)

    # Solicito al usuario que indique que opcion desea ejecutar.
    seleccion = input("Seleccione una opción (1/2/3/4/5/6/7): ")

    # Utilizo match para ejecutar el bloque correspondiente a la opcion elegida.
    match seleccion:

        # ------------------------------------------------------------
        # OPCION 1: AGREGAR UN PRODUCTO
        # ------------------------------------------------------------
        case "1":
            print("Agregar producto")

            # Solicito el identificador del producto.
            # La funcion solicitar_dato evita que el campo quede vacio.
            codigo_nuevo = solicitar_dato("ID")

            # Solicito el nombre del producto.
            nombre_nuevo = solicitar_dato("nombre")

            # Solicito la categoria del producto.
            categoria_nueva = solicitar_dato("categoria")

            # Solicito una descripcion del producto.
            descripcion_nueva = solicitar_dato("descripcion")

            # Solicito la cantidad de unidades disponibles.
            cantidad_nueva = solicitar_dato("cantidad")

            # Solicito el precio del producto.
            precio_nuevo = solicitar_dato("precio")

            # Creo una nueva lista con todos los datos ingresados.
            nuevo_producto = [
                codigo_nuevo,
                nombre_nuevo,
                categoria_nueva,
                descripcion_nueva,
                cantidad_nueva,
                precio_nuevo
            ]

            # Informo que el producto fue agregado y muestro sus datos.
            print("El producto se ha agregado con éxito:")
            mostrar_ficha(
                codigo_nuevo,
                nombre_nuevo,
                categoria_nueva,
                descripcion_nueva,
                cantidad_nueva,
                precio_nuevo
            )

            # Agrego la lista del nuevo producto al stock general.
            stock.append(nuevo_producto)


        # ------------------------------------------------------------
        # OPCION 2: MOSTRAR TODOS LOS PRODUCTOS
        # ------------------------------------------------------------
        case "2":
            print("Mostrar productos")

            # Recorro todos los productos que contiene la lista stock.
            for producto_actual in stock:

                # En cada vuelta, producto_actual representa una lista
                # con los datos de un producto.
                # Muestro sus datos utilizando las posiciones de esa lista.
                mostrar_ficha(
                    producto_actual[0],  # Posicion 0: identificador.
                    producto_actual[1],  # Posicion 1: nombre.
                    producto_actual[2],  # Posicion 2: categoria.
                    producto_actual[3],  # Posicion 3: descripcion.
                    producto_actual[4],  # Posicion 4: cantidad.
                    producto_actual[5]   # Posicion 5: precio.
                )


        # ------------------------------------------------------------
        # OPCION 3: BUSCAR UN PRODUCTO POR SU NOMBRE
        # ------------------------------------------------------------
        case "3":
            print("Buscar productos")

            # Pregunto al usuario que producto desea encontrar.
            nombre_a_buscar = input("Ingrese producto a buscar: ")

            # Creo una variable booleana que inicialmente vale False.
            # Cambiara a True si encuentro un producto con ese nombre.
            producto_encontrado = False

            # Recorro uno por uno todos los productos del stock.
            for producto_actual in stock:

                # Comparo el nombre ingresado con la posicion 1,
                # que es donde se guarda el nombre de cada producto.
                if nombre_a_buscar == producto_actual[1]:

                    # Si coinciden, informo que encontre el producto.
                    print("El Producto ha sido encontrado")

                    # Muestro toda la informacion del producto encontrado.
                    mostrar_ficha(
                        producto_actual[0],
                        producto_actual[1],
                        producto_actual[2],
                        producto_actual[3],
                        producto_actual[4],
                        producto_actual[5]
                    )

                    # Como encontre el producto, cambio la variable a True.
                    producto_encontrado = True

            # Si despues de recorrer el stock sigue en False,
            # significa que no encontre ningun producto con ese nombre.
            if producto_encontrado == False:
                print("El Producto NO EXISTE!")


        # ------------------------------------------------------------
        # OPCION 4: ACTUALIZAR LOS DATOS DE UN PRODUCTO
        # ------------------------------------------------------------
        case "4":
            print("Actualizar Producto")

            # Solicito el nombre del producto que se quiere modificar.
            nombre_a_buscar = input(
                "Ingrese Producto a actualizar: "
            )

            # Inicializo la variable en False para saber si encuentro el producto.
            producto_encontrado = False

            # Recorro todos los productos almacenados en el stock.
            for producto_actual in stock:

                # Verifico si el nombre ingresado coincide con el nombre
                # guardado en la posicion 1 del producto actual.
                if nombre_a_buscar == producto_actual[1]:

                    # Informo que encontre el producto.
                    print("El Producto ha sido encontrado")

                    # Muestro los datos actuales antes de modificarlos.
                    mostrar_ficha(
                        producto_actual[0],
                        producto_actual[1],
                        producto_actual[2],
                        producto_actual[3],
                        producto_actual[4],
                        producto_actual[5]
                    )

                    # Indico que el producto fue encontrado.
                    producto_encontrado = True

                    # Muestro los campos que el usuario puede actualizar.
                    print("""
                    1. Nombre
                    2. Categoria
                    3. Descripcion
                    4. Cantidad
                    5. Precio
                    6. Nada
                    """)

                    # Pregunto cual de los campos desea modificar.
                    campo_a_modificar = input(
                        "Ingrese opción a actualizar? 1/2/3/4/5/6: "
                    )

                    # Utilizo otro match para identificar el campo elegido.
                    match campo_a_modificar:

                        # Si elige 1, modifico el nombre del producto.
                        case "1":
                            print("Modificar el nombre")

                            # Elimino el valor que se encuentra en la posicion 1.
                            producto_actual.pop(1)

                            # Solicito el nuevo nombre.
                            nombre_actualizado = solicitar_dato("Ingresar Nuevo nombre")

                            # Inserto el nuevo nombre nuevamente en la posicion 1.
                            producto_actual.insert(1, nombre_actualizado)

                            # Informo que la modificacion se realizo correctamente.
                            print("El Producto fue modificado con éxito")

                        # Si elige 2, modifico la categoria.
                        case "2":
                            print("Modificar la categoria")

                            # Elimino la categoria anterior, ubicada en la posicion 2.
                            producto_actual.pop(2)

                            # Solicito la nueva categoria.
                            categoria_actualizada = solicitar_dato("Ingresar Nueva categoria")

                            # Inserto la nueva categoria en la posicion 2.
                            producto_actual.insert(2, categoria_actualizada)

                            # Informo que la modificacion se realizo correctamente.
                            print("El Producto se ha modificado correctamente")

                        # Si elige 3, modifico la descripcion.
                        case "3":
                            print("Modificar descripcion")

                            # Elimino la descripcion anterior, ubicada en la posicion 3.
                            producto_actual.pop(3)

                            # Solicito la nueva descripcion.
                            descripcion_actualizada = solicitar_dato("Ingresar Nueva descripcion")

                            # Inserto la nueva descripcion en la posicion 3.
                            producto_actual.insert(3, descripcion_actualizada)

                            # Informo que la modificacion se realizo correctamente.
                            print("El Producto se ha modificado correctamente")

                        # Si elige 4, modifico la cantidad disponible.
                        case "4":
                            print("Modificar cantidad")

                            # Elimino la cantidad anterior, ubicada en la posicion 4.
                            producto_actual.pop(4)

                            # Solicito la nueva cantidad.
                            cantidad_actualizada = solicitar_dato("Ingresar Nueva cantidad")

                            # Inserto la nueva cantidad en la posicion 4.
                            producto_actual.insert(4, cantidad_actualizada)

                            # Informo que la modificacion se realizo correctamente.
                            print("El Producto se ha modificado correctamente")

                        # Si elige 5, modifico el precio.
                        case "5":
                            print("Modificar precio")

                            # Elimino el precio anterior, ubicado en la posicion 5.
                            producto_actual.pop(5)

                            # Solicito el nuevo precio.
                            precio_actualizado = solicitar_dato("Ingresar Nuevo precio")

                            # Inserto el nuevo precio en la posicion 5.
                            producto_actual.insert(5, precio_actualizado)

                            # Informo que la modificacion se realizo correctamente.
                            print("El Producto se ha modificado correctamente")

                        # Si elige 6, no realizo ninguna modificacion.
                        case "6":
                            print("Ha seleccionado, NO actualizar ningún campo")

                        # Si ingresa otra opcion, informo que no es valida.
                        case _:
                            print("Ha ingresado una Opcion no valida")

            # Si no se encontro el producto durante el recorrido,
            # informo que no existe un producto con ese nombre.
            if producto_encontrado == False:
                print("El Producto no fue encontrado")


        # ------------------------------------------------------------
        # OPCION 5: ELIMINAR UN PRODUCTO
        # ------------------------------------------------------------
        case "5":
            print("Eliminar productos")

            # Pregunto que producto desea eliminar el usuario.
            nombre_a_eliminar = input("Ingrese el Producto a eliminar ")

            # Recorro los productos que se encuentran en el stock.
            for producto_actual in stock:

                # Comparo el nombre ingresado con el nombre del producto actual.
                if nombre_a_eliminar == producto_actual[1]:

                    # Informo que encontre el producto solicitado.
                    print("El Producto fue encontrado")

                    # Muestro los datos del producto antes de eliminarlo.
                    mostrar_ficha(
                        producto_actual[0],
                        producto_actual[1],
                        producto_actual[2],
                        producto_actual[3],
                        producto_actual[4],
                        producto_actual[5]
                    )

                    # Informo que se esta eliminando el producto.
                    print("Eliminando Producto...")

                    # Elimino de stock la lista correspondiente al producto.
                    stock.remove(producto_actual)


        # ------------------------------------------------------------
        # OPCION 6: GENERAR UN REPORTE DE STOCK
        # ------------------------------------------------------------
        case "6":
            print("Generación de Reporte de stock")

            # Pregunto cual es la cantidad que se considera stock minimo.
            # Con int convierto el texto ingresado a un numero entero.
            limite_de_stock = int(input("Ingrese Stock minimo: "))

            # Recorro todos los productos del stock.
            for producto_actual in stock:

                # Comparo la cantidad del producto (posicion 4)
                # con el limite minimo indicado por el usuario.
                if producto_actual[4] < limite_de_stock:

                    # Informo que se muestran productos por debajo del limite.
                    print(f"Productos con stock menor a {limite_de_stock}")

                    # Muestro la ficha del producto que cumple la condicion.
                    mostrar_ficha(
                        producto_actual[0],
                        producto_actual[1],
                        producto_actual[2],
                        producto_actual[3],
                        producto_actual[4],
                        producto_actual[5]
                    )


        # ------------------------------------------------------------
        # OPCION 7: SALIR DEL PROGRAMA
        # ------------------------------------------------------------
        case "7":

            # Muestro un mensaje de despedida.
            # Al volver al while, la condicion sera falsa y el bucle terminara.
            print("Ha seleccionado salir del Programa")


        # ------------------------------------------------------------
        # OPCION NO VALIDA
        # ------------------------------------------------------------
        case _:

            # Este bloque se ejecuta si el usuario ingresa una opcion
            # que no coincide con ninguna de las opciones del menu.
            print("La opción ingresada es incorrecta")
