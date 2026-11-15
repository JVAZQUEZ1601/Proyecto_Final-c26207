# Proyecto Final - SISTEMA DE GESTIÓN DE PRODUCTOS
# Autor: Julio Alejandro Vázquez.
# Comisión #26207

## Requerimientos

Crear una estructura de datos llamada `Stock`, para almacenar los datos
de los productos.

La estructura puede implementarse mediante una tabla o un diccionario,
según lo indicado en la consigna.

## Datos de los productos

Cada producto debe contemplar los siguientes campos:

  Campo           Descripción
  --------------- -------------------------------------------
  `id`            Identificador único del producto.
  `nombre`        Nombre del producto.
  `descripcion`   Breve descripción del producto.
  `cantidad`      Cantidad disponible del producto.
  `precio`        Precio del producto.
  `categoria`     Categoría a la que pertenece el producto.

## Funcionalidades de la aplicación

a- Registrar nuevos productos.
b- Visualizar datos de los productos registrados.
c- Actualizar datos de productos, mediante su ID.
d- Eliminación de productos, mediante su ID.
e- Búsqueda de productos, mediante su ID. De manera opcional, se puede implementar la búsqueda por los campos nombre o categoría.
f- Reporte de productos que tengan una cantidad igual o inferior a un límite especificado por el usuario.

## Requisitos técnicos

-El código debe estar bien estructurado, utilizando funciones para modularizar la lógica de la aplicación.
-Los comentarios deben estar presentes en el código, explicando las partes clave del mismo.