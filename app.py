import mysql.connector

class Catalogo:

  def __init__(self, host, user, password, database):

    self.conn = mysql.connector.connect(
      host=host,
      #port=port,
      user=user,
      password=password,
      database=database     
    )

    self.cursor = self.conn.cursor(dictionary=True)
    self.cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
      codigo INT AUTO_INCREMENT PRIMARY KEY,
      descripcion VARCHAR(255) NOT NULL,
      cantidad INT NOT NULL,
      precio DECIMAL(10, 2) NOT NULL,
      imagen_url VARCHAR(255),
      proveedor INT(4)''')
    self.conn.commit()

  def agregar_producto(self, codigo, description, cantidad, precio, imagen, proveedor):
    sql = "INSERT productos (descripcion, cantidad,precio, imagen, proveedor) VALUES (%s, %s, %s, %s, %s)"
    valores = (description, cantidad, precio, imagen, proveedor)

    self.cursor.execute(sql, valores)
    self.conn.commit()
    return self.cursor.lastrowid


#lista para productos
productos = [] 


def agregar_producto(codigo, descripcion, cantidad, precio, imagen, proveedor):

  if consultar_producto(codigo):
    return False

  nuevo_producto = {
    'codigo':codigo,
    'descripcion':descripcion,
    'cantidad':cantidad,
    'precio':precio,
    'imagen':imagen,
    'proveedor':proveedor
  }  

  productos.append(nuevo_producto)

  return True

#Esta función se encarga de buscar y recuperar la información de un producto de acuerdo a su código
def consultar_producto(codigo):
  for producto in productos:
    if producto['codigo'] == codigo:
      return producto
  return False

#Esta función se encarga de actualizar los datos de un producto existente en función de su código.
def modificar_producto(codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, nuevo_proveedor):
  for producto in productos:
    if producto['codigo'] == codigo:
      producto['descripcion'] =nueva_descripcion
      producto['cantidad'] = nueva_cantidad
      producto['precio'] = nuevo_precio
      producto['imagen'] = nueva_imagen
      producto['proveedor'] = nuevo_proveedor
      return True  
  return False

#Esta función tiene como objetivo mostrar en pantalla un listado de los productos almacenados
#en la aplicación de gestión de inventario.
def listar_productos():
  print("-" * 50)

  for producto in productos:
    print(f" codigo......: {producto['codigo']} ")
    print(f" descripcion.: {producto['descripcion']} ")
    print(f" cantidad....: {producto['cantidad']}")
    print(f" precio......: {producto['precio']} ")
    print(f" imagen......: {producto['imagen']} ")
    print(f" proveedor...: {producto['proveedor']} ")
    print("-" * 50)

#Esta función tiene la responsabilidad de eliminar un producto específico de la lista de productos
#en la aplicación de gestión de inventario.
def eliminar_producto(codigo):
  for producto in productos:
    if producto['codigo'] == codigo :
      productos.remove(producto)
      return True
  return False


#Agregarmos productos  ala lista

agregar_producto(1, "Mouse optico", 100, 15500.50, "imagen.jpg","Rumania")
agregar_producto(2, "teclado optico", 58, 26000.50,"imagen.jpg", "Mania")
agregar_producto(3, "pad optico", 300, 155.50, "imagen.jpg","Vaultec")
agregar_producto(4, "impresoa", 400, 15550.50, "imagen.jpg","Checa")
agregar_producto(5, "Mando", 250, 15500, "imagen.jpg","Peru")

# listar_productos()

# #consultar Producto
# codigo_pro = int(input("Ingrese el codigo del producto: "))
# producto = consultar_producto(codigo_pro)

# if producto:
#   print(f"Producto encontraso {producto['codigo']} - {producto['descripcion']}")
# else:
#   print(f"Producto con codigo {codigo_pro} no encontrado")

# modificar_producto(5, "Mando peruano", 99, 8522.20,"causa.jpg","Peru Tic")

# print("#"*50)
# #listar productos de nuevo
# listar_productos()

# #eliminar producto
# eliminar_producto(5)

# print("*"*50)
# #listamos productos de nuevo
# listar_productos()

catalogo = Catalogo(host= 'localhost', user='root', password='root', database='miapp')
