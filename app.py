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
      proveedor INT(4))''')
    self.conn.commit()
  
  def consultar_producto(self, codigo):
    self.cursor.execute(f"SELECT * FROM productos WHERE codigo = {codigo}")
    return self.cursor.fetchone()

  def agregar_producto(self, description, cantidad, precio, imagen, proveedor):
    sql = "INSERT productos (descripcion, cantidad,precio, imagen_url, proveedor) VALUES (%s, %s, %s, %s, %s)"
    valores = (description, cantidad, precio, imagen, proveedor)

    self.cursor.execute(sql, valores)
    self.conn.commit()
    return self.cursor.lastrowid
  
  def modificar_producto(self, codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen,nuevo_proveedor ):
    sql = "UPDATE productos SET descripcion = %s, cantidad=%s, precio=%s, imagen_url=%s, proveedor=%s WHERE codigo=%s"
    valores = (nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, nuevo_proveedor, codigo)
    self.cursor.execute(sql, valores)
    self.conn.commit()

    return self.cursor.rowcount > 0
  
  def mostrar_producto(self, codigo):
    producto = self.consultar_producto(codigo)
    if producto:
      print( "-" * 40 )
      print(f"Codigo.......:{producto['codigo']}")
      print(f"Descripcion..:{producto['descripcion']}")
      print(f"Cantidad.....:{producto['cantidad']}")
      print(f"Precio.......:{producto['precio']}")
      print(f"Proveedor....:{producto['imagen_url']}")
      print(f"Imagen.......:{producto['proveedor']}")
      print("-" * 40)
    else:
      print("Producto no encontrado")

  def listar_productos(self):
    self.cursor.execute("SELECT * FROM productos")
    productos = self.cursor.fetchall()
    return productos
  
  def eliminar_producto(self, codigo):
    self.cursor.execute(f"DELETE FROM productos WHERE codigo = {codigo}")
    return self.cursor.rowcount


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

catalogo = Catalogo(host= 'localhost', user='root', password='', database='miapp')
catalogo.agregar_producto("taclado Qwerty",15, 11000.0, 'teclado.jpg', 21 )
catalogo.agregar_producto("taclado Led ",25, 19000.0, 'teclado_RGB.jpg', 200 )


#onsultamos un productos y lo mostramos
#cod_pro = int(input("Ingrese el codigo del producto"))
#producto = catalogo.consultar_producto(cod_pro)
producto = catalogo.modificar_producto(2,"Mouse con bolitasss",8, 55000.0, 'Mouse_Colita.jpg', 300 )
print(producto)
if producto:
  print(f"Producto encontrado")
else: 
  print(f"Producto no encontrado")
catalogo.mostrar_producto(200)
catalogo.eliminar_producto(2)
productos = catalogo.listar_productos()

for producto in productos:
  print(producto)
