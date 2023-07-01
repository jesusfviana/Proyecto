from Producto import Producto
from Venta import Venta
from Pago import Pago
from Envio import Envio
from ClienteNatural import ClienteNatural
from ClienteJuridico import ClienteJuridico
from Validaciones import Validaciones
from OrdenCompra import OrdenCompra
from Motorizado import Motorizado
import pickle
import os
from datetime import datetime, timedelta
from collections import Counter



class Funciones:
    
    def __init__(self):
        """Constructor de la clase.

    Args:
        No se requieren argumentos.

    Returns:
        No devuelve ningún valor.

    Raises:
        No se producen excepciones.

    La función instancia un objeto de la clase Validaciones y lo almacena en el atributo 'validaciones' del objeto de la
    clase que se está creando.
        """
        self.validaciones = Validaciones()



# TXT////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def read_txt(self, archivo, lista):
        """Lee datos de un archivo de texto con formato pickle y los almacena en una lista.

    Args:
        archivo: ruta del archivo de texto con formato pickle que se va a leer.
        lista: lista en la que se van a almacenar los datos leídos.

    Returns:
        No devuelve ningún valor.

    Raises:
        No se producen excepciones.

    La función verifica si el archivo de texto con formato pickle tiene un tamaño mayor que cero. Si es así, abre el archivo
    en modo de lectura binaria, utiliza la función pickle.load() para cargar los datos del archivo en la lista especificada
    y cierra el archivo.
        """
        if os.path.getsize(archivo) > 0:
            with open(archivo, "rb") as f:
                lista = pickle.load(f)

    def write_txt(self, archivo, lista):
        """Escribe datos en un archivo de texto con formato pickle.

    Args:
        archivo: ruta del archivo de texto con formato pickle en el que se van a escribir los datos.
        lista: lista que contiene los datos que se van a escribir en el archivo.

    Returns:
        No devuelve ningún valor.

    Raises:
        No se producen excepciones.

    La función abre el archivo en modo de escritura binaria, utiliza la función pickle.dump() para escribir los datos
    de la lista en el archivo y cierra el archivo.
        """
        with open(archivo, "wb") as f:
            pickle.dump(lista, f)



# 1.GESTION DE PRODUCTOS///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def agregar_producto(self, productos):
        """Permite agregar un nuevo producto a la lista de productos.

        Args:
        self: objeto de la clase App.
        productos: lista de objetos Producto existentes.

        Returns:
        None.

        Raises:
        No se producen excepciones.

        La función solicita al usuario que ingrese los datos del nuevo producto, valida los datos ingresados
        y crea un objeto Producto con ellos. Luego, agrega el objeto a la lista de productos y escribe la lista
        actualizada en el archivo 'productos.txt'. Finalmente, muestra un mensaje indicando que el producto ha
        sido agregado exitosamente.
        """
        nombre = self.validaciones.validar_alfabetico("Ingrese el nombre del producto: ").capitalize()
        descripcion = self.validaciones.validar_alfabetico("Ingrese la descripcion del producto: ")
        precio = self.validaciones.validar_flotante("Ingrese el precio del producto: ")
        categoria = self.validaciones.validar_alfabetico("Ingrese la categoria del producto: ").capitalize()
        inventario = self.validaciones.validar_entero("Ingrese la disponibilidad del producto: ")
        nuevo_producto = Producto(nombre, descripcion, precio, categoria, inventario)
        productos.append(nuevo_producto)

        self.write_txt("productos.txt", productos)

        print("PRODUCTO AGREGADO EXITOSAMENTE")

        
    def buscar_productos_por_categoria(self, productos):
        """Busca productos por categoría en una lista de productos.

    Args:
        productos: lista de productos en la que se va a buscar.

    Returns:
        No devuelve ningún valor.

    Raises:
        No se producen excepciones.

    La función utiliza el método 'validar_alfabetico' de la clase 'Validaciones' para solicitar al usuario la categoría
    de producto que desea buscar. Luego, recorre la lista de productos y muestra los productos que pertenecen a la
    categoría especificada. Si no se encuentra ningún producto en la categoría, muestra un mensaje indicando que no se
    encontró ningún producto.
        """
        buscar_producto_categoria = self.validaciones.validar_alfabetico("Ingrese la categoria del producto que desea buscar: ").capitalize()
        aux = False
        for producto in productos:
            if producto.get_categoria() == buscar_producto_categoria:
                aux = True 
                print(producto.show())
        if not aux:
            print("PRODUCTO NO ENCONTRADO")


    def buscar_productos_por_precio(self, productos):
        """Busca productos por rango de precio en una lista de productos.

    Args:
        productos: lista de productos en la que se va a buscar.

    Returns:
        No devuelve ningún valor.

    Raises:
        Exception: si el precio mínimo ingresado es mayor o igual al precio máximo.

    La función utiliza el método 'validar_flotante' de la clase 'Validaciones' para solicitar al usuario el precio mínimo
    y máximo que desea buscar. Si el precio mínimo es mayor o igual al precio máximo, se genera una excepción. Luego,
    recorre la lista de productos y muestra los productos que tienen un precio dentro del rango especificado. Si no se
    encuentra ningún producto en el rango de precios, muestra un mensaje indicando que no se encontró ningún producto.
        """
        inf = self.validaciones.validar_flotante("Ingrese un precio minimo: ")
        sup = self.validaciones.validar_flotante("Ingrese un precio maximo: ")
        aux = False
        if inf >= sup:
            raise Exception
        for producto in productos: 
                if inf <= producto.get_precio() <= sup:
                    aux = True
                    print(producto.show())
        if not aux:
            print("PRODUCTO NO ENCONTRADO")


    def buscar_productos_por_nombre(self, productos):
        """Busca productos por nombre en una lista de productos.

    Args:
        productos: lista de productos en la que se va a buscar.

    Returns:
        No devuelve ningún valor.

    Raises:
        No se producen excepciones.

    La función utiliza el método 'validar_alfabetico' de la clase 'Validaciones' para solicitar al usuario el nombre
    del producto que desea buscar. Luego, recorre la lista de productos y muestra los productos que tienen el nombre
    especificado. Si no se encuentra ningún producto con el nombre especificado, muestra un mensaje indicando que no
    se encontró ningún producto.
        """
        buscar_producto_nombre = self.validaciones.validar_alfabetico("Ingrese el nombre del producto que desea buscar: ").capitalize()
        aux = False
        for producto in productos: 
            if producto.get_nombre() == buscar_producto_nombre:
                aux = True
                print(producto.show())
        if not aux:
            print("PRODUCTO NO ENCONTRADO")


    def buscar_productos_por_disponibilidad_en_inventario(self, productos):
        """ Busca productos por disponibilidad en inventario en una lista de productos.

    Args:
        productos: lista de productos en la que se va a buscar.

    Returns:
        No devuelve ningún valor.

    Raises:
        No se producen excepciones.

    La función utiliza un ciclo 'while' y el método 'input' para solicitar al usuario que indique si desea buscar productos
    disponibles o agotados. Se utiliza un bloque 'try-except' para validar que el usuario ingrese un valor numérico válido.
    Luego, recorre la lista de productos y muestra los productos que están disponibles o agotados, según lo que haya
    indicado el usuario. Si no se encuentra ningún producto con la disponibilidad especificada, muestra un mensaje indicando
    que no se encontró ningún producto.
        """
        while True:
            try:
                o = int(input("""
                Indique que productos desea buscar: 
                1. Productos Disponibles
                2. Productos Agotados
                """))
                if o < 1 or o > 2:
                    raise ValueError
            except:
                print("ERROR: Dato invalido, intente de nuevo")
                continue
        
            if o == 1:
                for producto in productos:
                    if producto.get_inventario_disponible() > 0:
                        print(producto.show())
            elif o == 2:
                for producto in productos:
                    if producto.get_inventario_disponible() == 0:
                        print(producto.show())


    def modificar_producto(self, productos):
        """Modifica un producto en una lista de productos.

    Args:
        productos: lista de productos en la que se va a buscar y modificar.

    Returns:
        No devuelve ningún valor.

    Raises:
        No se producen excepciones.

    La función utiliza un ciclo 'while' y el método 'input' para solicitar al usuario que indique qué atributo desea
    modificar del producto. Se utiliza un bloque 'try-except' para validar que el usuario ingrese un valor numérico válido.
    Luego, recorre la lista de productos y muestra los productos disponibles. Solicita al usuario que indique qué producto
    desea modificar y luego valida que el producto seleccionado exista en la lista. Luego, dependiendo de lo que haya
    indicado el usuario, se modifica el atributo correspondiente del producto seleccionado y se guarda la lista de productos
    modificada en un archivo de texto. Si no se encuentra el producto seleccionado, muestra un mensaje indicando que no
    se encontró ningún producto.

        """
        print("Modificar Producto")
        while True: 
            try:
                m = int(input("""
                Ingrese la opcion de lo que desea modificar:
                1. Nombre
                2. Descripcion
                3. Precio
                4. Categoria
                5. Inventario Disponible
                6. Producto Completo
                7. Volver al menu
                """)) 

                if m < 1 or m > 7:
                    raise ValueError
            except:
                print("ERROR: Dato invalido, intente de nuevo")
                continue

            if m == 1: #NOMBRE//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                for producto in productos:
                    print(producto.show())
                nombre_producto_seleccionado = self.validaciones.validar_alfabetico("Indique el nombre del producto que desea modificar: ").capitalize()
                aux = False
                for producto in productos:
                    if producto.get_nombre() == nombre_producto_seleccionado: 
                        aux = True
                        n_nombre =  self.validaciones.validar_alfabetico("Ingrese el nuevo nombre del producto: ").capitalize()
                        producto.set_nombre(n_nombre)
                        self.write_txt("productos.txt", productos)
                        print("PRODUCTO MODIFICADO EXITOSAMENTE!!")
                        print(producto.show())
                        break
                if not aux:
                    print("PRODUCTO NO ENCONTRADO")


            elif m == 2: #DESCRIPCION//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                for producto in productos:
                    print(producto.show())
                nombre_producto_seleccionado = self.validaciones.validar_alfabetico("Indique el nombre del producto que desea modificar: ").capitalize()
                aux = False
                for producto in productos:
                    if producto.get_nombre() == nombre_producto_seleccionado:
                        aux = True
                        n_descripcion = self.validaciones.validar_alfabetico("Ingrese la nueva descripcion del producto: ")
                        producto.set_descripcion(n_descripcion)
                        self.write_txt("productos.txt", productos)
                        print("PRODUCTO MODIFICADO EXITOSAMENTE!!")
                        print(producto.show())
                        break
                if not aux:
                    print("PRODUCTO NO ENCONTRADO")


            elif m == 3: #PRECIO//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                for producto in productos:
                    print(producto.show())
                nombre_producto_seleccionado = self.validaciones.validar_alfabetico("Indique el nombre del producto que desea modificar: ").capitalize()
                aux = False
                for producto in productos:
                    if producto.get_nombre() == nombre_producto_seleccionado:
                        aux = True
                        n_precio = self.validaciones.validar_flotante("Ingrese el nuevo precio del producto: ")
                        producto.set_precio(n_precio)
                        self.write_txt("productos.txt", productos)
                        print("PRODUCTO MODIFICADO EXITOSAMENTE!!")
                        print(producto.show())
                        break
                if not aux:
                    print("PRODUCTO NO ENCONTRADO")


            elif m == 4: #CATEGORIA//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                for producto in productos:
                    print(producto.show())
                nombre_producto_seleccionado = self.validaciones.validar_alfabetico("Indique el nombre del producto que desea modificar: ").capitalize()
                aux = False
                for producto in productos:
                    if producto.get_nombre() == nombre_producto_seleccionado:
                        aux = True
                        n_categoria = self.validaciones.validar_alfabetico("Ingrese la nueva categoria del producto: ")
                        producto.set_categoria(n_categoria)
                        self.write_txt("productos.txt", productos)
                        print("PRODUCTO MODIFICADO EXITOSAMENTE!!")
                        print(producto.show())
                        break
                if not aux:
                    print("PRODUCTO NO ENCONTRADO")


            elif m == 5: #INVENTARIO//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                for producto in productos:
                    print(producto.show())
                nombre_producto_seleccionado = self.validaciones.validar_alfabetico("Indique el nombre del producto que desea modificar: ").capitalize()
                aux = False
                for producto in productos:
                    if producto.get_nombre() == nombre_producto_seleccionado:
                        aux = True 
                        n_inventario_disponible = self.validaciones.validar_entero("Ingrese el nuevo inventario_disponible del producto: ")
                        producto.set_inventario_disponible(n_inventario_disponible)
                        self.write_txt("productos.txt", productos)
                        print("PRODUCTO MODIFICADO EXITOSAMENTE!!")
                        print(producto.show())
                        break
                if not aux:
                    print("PRODUCTO NO ENCONTRADO")


            elif m == 6: #COMPLETO//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                for producto in productos:
                    print(producto.show())
                nombre_producto_seleccionado = self.validaciones.validar_alfabetico("Indique el nombre del producto que desea modificar: ").capitalize()
                aux = False
                for producto in productos:
                    if producto.get_nombre() == nombre_producto_seleccionado:
                        aux = True
                        n_nombre = self.validaciones.validar_alfabetico("Ingrese el nuevo nombre del producto: ").capitalize()
                        n_descripcion = self.validaciones.validar_alfabetico("Ingrese la nueva descripcion del producto: ")
                        n_precio = self.validaciones.validar_flotante("Ingrese el nuevo precio del producto: ")
                        n_categoria = self.validaciones.validar_alfabetico("Ingrese la nueva categoria del producto: ").capitalize()
                        n_inventario_disponible =  self.validaciones.validar_entero("Ingrese el nuevo inventario_disponible del producto: ")
                        producto.set_nombre(n_nombre)
                        producto.set_descripcion(n_descripcion)
                        producto.set_precio(n_precio)
                        producto.set_categoria(n_categoria)
                        producto.set_inventario_disponible(n_inventario_disponible)
                        self.write_txt("productos.txt", productos)
                        print("PRODUCTO MODIFICADO EXITOSAMENTE!!")
                        print(producto.show())
                        break
                if not aux:
                    print("PRODUCTO NO ENCONTRADO")


            elif m == 7: #VOLVER MENU PRINCIPAL//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                break


    def eliminar_productos(self, productos):
        """Elimina un producto de una lista de productos.

    Args:
        productos: lista de productos en la que se va a buscar y eliminar.

    Returns:
        No devuelve ningún valor.

    Raises:
        No se producen excepciones.

    La función recorre la lista de productos y muestra los productos disponibles. Solicita al usuario que indique qué producto
    desea eliminar y luego valida que el producto seleccionado exista en la lista. Si el producto existe en la lista, se elimina
    de la lista de productos y se guarda la lista de productos modificada en un archivo de texto. Si no se encuentra el producto
    seleccionado, muestra un mensaje indicando que no se encontró ningún producto.
        """
        for producto in productos:
            print(producto.show())
        eliminar = self.validaciones.validar_alfabetico("Ingrese el nombre del producto que desea eliminar: ")
        aux = False
        for producto in productos: 
             if producto.get_nombre() == eliminar:
                aux = True
                productos.remove(producto)
                self.write_txt("productos.txt", productos)
                print(producto.show())
                print("PRODUCTO ELIMINADO")
                break
        if not aux:
            print("PRODUCTO NO ENCONTRADO")
       


    # 2.GESTION DE VENTAS////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def registro_ventas(self, ventas, productos, envios, pagos):
        """Registra una venta en el sistema.

    Argumentos:
    - ventas: lista de ventas registradas en el sistema
    - productos: lista de productos disponibles en el sistema
    - envios: lista de envíos realizados por la empresa
    - pagos: lista de pagos registrados en el sistema

    El método solicita al usuario ingresar el tipo de cliente que va a registrar (jurídico o natural). 
    Luego, solicita los datos necesarios para registrar la venta correspondiente al cliente, incluyendo 
    los productos vendidos, la dirección de envío y el método de pago utilizado. 

    Si todos los datos son válidos, la venta se registra en el sistema y se actualizan las listas de 
    ventas, productos, envíos y pagos. Si los datos son inválidos, se muestra un mensaje de error y se 
    solicitan nuevamente.

    Este método no devuelve ningún valor.
        """
        while True:
            try:
                tipo_cliente = int(input("""
                Ingrese el tipo de Cliente que va a registrar:
                1.Juridico
                2.Natural
                """))
                if tipo_cliente < 1 or tipo_cliente > 2:
                    raise ValueError
            except:
                print("ERROR: Dato invalido, intente de nuevo")
                continue
            
            if tipo_cliente == 1: #JURIDICO
                cliente = self.validaciones.validar_flotante("Ingrese el rif del cliente: ")
                if cliente.isinstance(ClienteJuridico) and cliente.get_rif() == cliente:
                    for producto in productos:
                        print(producto.show())
                    carrito = []
                    while True:
                        produ = input("Ingrese el nombre del producto que va a comprar: ")
                        produ_encontrado = None
                        for producto in productos:
                            if producto.get_nombre() == produ:
                                produ_encontrado = producto
                                break
                        if produ_encontrado:
                            try:  
                                cant = int(input("Ingrese la cantidad que llevara de este producto: "))
                            except:
                                print("ERROR: Dato invalido, intente de nuevo")
                                continue
                            item = {"producto": produ_encontrado.nombre, "cantidad": cant, "descripcion": produ_encontrado.descripcion, "precio": produ_encontrado.precio}
                            carrito.append(item)
                            print("Producto agregado al carrito.")

                        else:
                            print("El producto ingresado no está en el inventario.")
                            carrito.append({produ,cant})
                                
                        try:
                            cont = int(input("""
                            Desea continuar?
                            1. Si
                            2. No
                            """))
                            if cont < 1 or cont > 2:
                                raise ValueError
                        except:
                            print("ERROR: Dato invalido, intente de nuevo")
                            continue
                        if cont == 1:
                            continue
                        elif cont == 2:
                            break
                    #METODO ENVIO 
                    while True:
                        try:
                            c = int(input("""
                            Desea registar el envio?
                            1. Si
                            2. No
                            """))
                            if c < 1 or c > 2:
                                raise ValueError
                        except:
                            print("ERROR: Dato invalido, intente de nuevo")
                            continue

                        if c == 1: #CONTINUAR CON ENVIO ///////////////////////////////////////////////////
                            try:
                                met_pago =  int(input("""
                                Indique el tipo de pago: 
                                1.Punto de Venta
                                2.Pago Movil
                                3.Zelle
                                4.Cash
                                """))
                                if met_pago < 1 or met_pago > 2:
                                    raise ValueError
                            except:
                                print("ERROR: Dato invalido, intente de nuevo")
                                continue
                            if met_pago == "1":
                                tipo = ("Punto de Venta")
                            elif met_pago == "2":
                                tipo = ("Pago Movil")
                            elif met_pago == "3":
                                tipo = ("Zelle")
                            elif met_pago == "4":
                                tipo = ("Cash")
                            noc = OrdenCompra(cliente, carrito, tipo)
                            try:
                                ops_envio = int(input("""
                                    Seleccione el servicio de envio: 
                                    1. MRW 5$
                                    2. Zoom 7$
                                    3. Delivery 10$
                                    """))
                                if ops_envio < 1 or ops_envio > 3:
                                    raise ValueError
                            except:
                                print("ERROR: Dato invalido, intente de nuevo")
                                continue
                            if ops_envio == "1":
                                envio = ("MRW")
                                costo_servicio = 5
                            elif ops_envio == "2":
                                envio = ("Zoom")
                                costo_servicio = 7
                            elif ops_envio == "3":
                                envio = ("Delivery")
                                costo_servicio = 10
                                nombre = input("Ingrese el nombre del motorizado del delivery: ")
                                telf = input("Ingrese el telefono del delivery: ")
                                motorizado = Motorizado(nombre, telf)
                            fecha = datetime.date.today()
                            envio = Envio(noc, envio, motorizado, costo_servicio, fecha)
                            envios.append(envio)
                            self.write_txt("envios.txt", envios)
                            while True:
                                try:
                                    en = int(input("""
                                    Desea registar el pago?
                                    1. Si
                                    2. No
                                    """))
                                    if en < 1 or en > 2:
                                        raise ValueError
                                except:
                                    print("ERROR: Dato invalido, intente de nuevo")
                                    continue
                                if en == 1:
                                    #METODO PAGO
                                    try:
                                        moneda = int(input("""
                                        Indique la moneda del pago: 
                                        1.Divisas
                                        2.Bolivares
                                        """)) 
                                        if moneda < 1 or moneda > 2:
                                            raise ValueError
                                    except:
                                        print("ERROR: Dato invalido, intente de nuevo")
                                        continue

                                    try:
                                        ops_tipo = int(input("""
                                                    Indique el tipo de pago: 
                                                    1.Punto de Venta
                                                    2.Pago Movil
                                                    3.Zelle
                                                    4.Cash
                                                    """))
                                        if ops_tipo < 1 or ops_tipo > 4:
                                            raise ValueError
                                    except:
                                        print("ERROR: Dato invalido, intente de nuevo")
                                        continue
                                    if ops_tipo == "1":
                                        tipo = ("Punto de Venta")
                                    elif ops_tipo == "2":
                                        tipo = ("Pago Movil")
                                    elif ops_tipo == "3":
                                        tipo = ("Zelle")
                                    elif ops_tipo == "4":
                                        tipo = ("Cash")
                                    subtotal = 0 
                                    for item in carrito:
                                        subtotal += item["precio"] * item["cantidad"]
                                    for producto in productos:
                                        for precio in productos:
                                            precio * cant(producto) == subtotal
                                    try:
                                        o = int(input("""
                                                    Pagara al contado?: 
                                                    1. Si
                                                    2. No
                                                    """))
                                        if o < 1 or o > 2:
                                            raise ValueError
                                    except:
                                        print("ERROR: Dato invalido, intente de nuevo")
                                        continue
                                    if o == 1:
                                        descuentos = subtotal * 0.05
                                    elif o == 2:
                                        descuentos = 0
                                    iva = subtotal * 0.16
                                    if moneda == 1:
                                        igtf = subtotal * 0.03
                                    elif moneda == 2:
                                        igtf = 0
                                    monto_total = subtotal + iva + igtf + costo_servicio - descuentos
                                    pago = Pago(cliente, monto_total, moneda, tipo, fecha)
                                    pagos.append(pago)
                                    self.write_txt("pagos.txt" , pagos)
                                elif en == 2:
                                    pago = 'pendiente'
                                
                        elif c == 2: #NO CONTINUAR CON ENVIO ///////////////////////////////////////////////
                            envio = 'pendiente'
                            pago = 'pendiente'
                            subtotal = 0 
                            for item in carrito:
                                subtotal += item["precio"] * item["cantidad"]
                            for producto in productos:
                                for precio in productos:
                                    precio * cant(producto) == subtotal
                            descuentos = "pendiente"
                            iva = "pendiente"
                            igtf = "pendiente"
                            monto_total = "pendiente"
                
                        nueva_venta = Venta(cliente, carrito, pago, envio, subtotal, descuentos,  iva, igtf, monto_total)
                        ventas.append(nueva_venta)
                        self.write_txt("ventas.txt", ventas)
                        #GENERAR FACTURA
                        print(nueva_venta.show())


            elif tipo_cliente == 2: #NATURAL
                cliente = self.validaciones.validar_fl("Ingres la cedula del cliente: ")
                if cliente.isinstance(ClienteNatural) and cliente.get_cedula() == cliente:
                    for producto in productos:
                        print(producto.show())
                    carrito = []
                    while True:
                        produ = input("Ingrese el nombre del producto que va a comprar: ")
                        produ_encontrado = None
                        for producto in productos:
                            if producto.get_nombre() == produ:
                                produ_encontrado = producto
                                break
                        if produ_encontrado:
                            try:  
                                cant = int(input("Ingrese la cantidad que llevara de este producto: "))
                            except:
                                print("ERROR: Dato invalido, intente de nuevo")
                                continue
                            item = {"producto": produ_encontrado.nombre, "cantidad": cant, "descripcion": produ_encontrado.descripcion, "precio": produ_encontrado.precio}
                            carrito.append(item)
                            print("Producto agregado al carrito.")

                        else:
                            print("El producto ingresado no está en el inventario.")
                            carrito.append({produ,cant})
                                
                        try:
                            cont = int(input("""
                            Desea continuar?
                            1. Si
                            2. No
                            """))
                            if cont < 1 or cont > 2:
                                raise ValueError
                        except:
                            print("ERROR: Dato invalido, intente de nuevo")
                            continue
                        if cont == 1:
                            continue
                        elif cont == 2:
                            break
                    #METODO ENVIO 
                    try:
                        met_pago =  int(input("""
                        Indique el tipo de pago: 
                        1.Punto de Venta
                        2.Pago Movil
                        3.Zelle
                        4.Cash
                        """))
                        if met_pago < 1 or met_pago > 2:
                            raise ValueError
                    except:
                        print("ERROR: Dato invalido, intente de nuevo")
                        continue
                    if met_pago == "1":
                        tipo = ("Punto de Venta")
                    elif met_pago == "2":
                        tipo = ("Pago Movil")
                    elif met_pago == "3":
                        tipo = ("Zelle")
                    elif met_pago == "4":
                        tipo = ("Cash")
                    noc = OrdenCompra(cliente, carrito, tipo)
                    try:
                        ops_envio = int(input("""
                            Seleccione el servicio de envio: 
                            1. MRW 5$
                            2. Zoom 7$
                            3. Delivery 10$
                            """))
                        if ops_envio < 1 or ops_envio > 3:
                            raise ValueError
                    except:
                        print("ERROR: Dato invalido, intente de nuevo")
                        continue
                    if ops_envio == "1":
                        envio = ("MRW")
                        costo_servicio = 5
                    elif ops_envio == "2":
                        envio = ("Zoom")
                        costo_servicio = 7
                    elif ops_envio == "3":
                        envio = ("Delivery")
                        costo_servicio = 10
                        nombre = input("Ingrese el nombre del motorizado del delivery: ")
                        telf = input("Ingrese el telefono del delivery: ")
                        motorizado = Motorizado(nombre, telf)
                    fecha = datetime.date.today()
                    envio = Envio(noc, envio, motorizado, costo_servicio, fecha)
                    envios.append(envio)
                    self.write_txt("envios.txt", envios)
                    #METODO PAGO
                    try:
                        moneda = int(input("""
                        Indique la moneda del pago: 
                        1.Divisas
                        2.Bolivares
                        """)) 
                        if moneda < 1 or moneda > 2:
                            raise ValueError
                    except:
                        print("ERROR: Dato invalido, intente de nuevo")
                        continue

                    try:
                        ops_tipo = int(input("""
                                    Indique el tipo de pago: 
                                    1.Punto de Venta
                                    2.Pago Movil
                                    3.Zelle
                                    4.Cash
                                    """))
                        if ops_tipo < 1 or ops_tipo > 4:
                            raise ValueError
                    except:
                        print("ERROR: Dato invalido, intente de nuevo")
                        continue
                    if ops_tipo == "1":
                        tipo = ("Punto de Venta")
                    elif ops_tipo == "2":
                        tipo = ("Pago Movil")
                    elif ops_tipo == "3":
                        tipo = ("Zelle")
                    elif ops_tipo == "4":
                        tipo = ("Cash")
                    subtotal = 0 
                    for item in carrito:
                        subtotal += item["precio"] * item["cantidad"]
                    for producto in productos:
                        for precio in productos:
                            precio * cant(producto) == subtotal
                    descuentos = 0
                    iva = subtotal * 0.16
                    if moneda == 1:
                        igtf = subtotal * 0.03
                    elif moneda == 2:
                        igtf = ("En los pagos en bolivares no aplica IGTF")
                    monto_total = subtotal + iva + igtf
                    pago = Pago(cliente, monto_total, moneda, tipo, fecha)
                    pagos.append(pago)
                    self.write_txt("pagos.txt", pagos)
                    nueva_venta = Venta(cliente, carrito, pago, envio, subtotal, descuentos,  iva, igtf, monto_total)
                    ventas.append(nueva_venta)
                    self.write_txt("ventas.txt", ventas)
                    #GENERAR FACTURA
                    print(nueva_venta.show())


    def buscar_venta_por_cliente(self, ventas):
        """ Busca una venta en la lista de ventas por el ID del cliente que la realizó.

    Argumentos:
    - self: instancia de la clase que contiene el método
    - ventas: lista de ventas registradas en el sistema

    El método solicita al usuario que ingrese el ID (cedula o rif) del cliente que desea buscar. 
    Luego, itera sobre la lista de ventas y verifica si la cedula o rif del cliente de cada venta 
    coincide con el ID ingresado. Si se encuentra una venta que coincide, se muestra su información 
    llamando al método "show" de la venta. Si no se encuentra ninguna venta, se muestra un mensaje 
    indicando que no se encontró ninguna venta.

    Este método no devuelve ningún valor.
        """
        buscar_cliente = self.validaciones.validar_flotante("Indique la cedula o rif del cliente que desea buscar: ")
        aux = False
        for venta in ventas: 
            if venta.get_cedula() or venta.get_rif() == buscar_cliente:
                aux = True
                print(venta.show())
        if not aux:
            print("VENTA NO ENCONTRADO")


    def buscar_venta_por_fecha(self, ventas):
        """Busca ventas en la lista de ventas que se encuentran en un rango de fechas.

    Argumentos:
    - self: instancia de la clase que contiene el método
    - ventas: lista de ventas registradas en el sistema

    El método solicita al usuario que ingrese dos fechas: la fecha de inicio y la fecha de fin de 
    la búsqueda. Luego, verifica si la fecha de cada venta en la lista de ventas se encuentra en 
    el rango de fechas especificado. Si la venta se encuentra en el rango de fechas, se agrega a 
    una lista de ventas dentro del rango. Al finalizar la búsqueda, se devuelve una lista con las 
    ventas que se encuentran en el rango de fechas.

    Si la fecha de inicio es mayor que la fecha de fin, se muestra un mensaje de error y se devuelve 
    una lista vacía.

    Retorna una lista de ventas que se encuentran en el rango de fechas especificado.
        """
        fecha_inicio = self.validaciones.validar_fecha("Ingresa la fecha desde donde quiere iniciar la busqueda (fecha en formato 'dd/mm/aaaa'):")
        fecha_fin = self.validaciones.validar_fecha("Ingresa la fecha hasta donde quiere la busqueda (fecha en formato 'dd/mm/aaaa'):")
        if fecha_inicio > fecha_fin:
            print("La fecha de inicio debe ser menor o igual que la fecha de fin.")
            return []

        ventas_rango_fechas = []
        for venta in ventas:
            if fecha_inicio <= venta.get_fecha() <= fecha_fin:
                ventas_rango_fechas.append(venta)
                return ventas_rango_fechas


    def buscar_venta_por_monto_total(self, ventas):
        """Busca ventas en la lista de ventas que se encuentran en un rango de monto total.

    Argumentos:
    - self: instancia de la clase que contiene el método
    - ventas: lista de ventas registradas en el sistema

    El método solicita al usuario que ingrese dos montos: el monto mínimo y el monto máximo de la 
    búsqueda. Luego, verifica si el monto total de cada venta en la lista de ventas se encuentra 
    en el rango de montos especificado. Si la venta se encuentra en el rango de montos, se agrega 
    a una lista de ventas dentro del rango. Al finalizar la búsqueda, se devuelve una lista con las 
    ventas que se encuentran en el rango de montos.

    Si el monto mínimo es mayor que el monto máximo, se muestra un mensaje de error y se devuelve 
    una lista vacía.

    Retorna una lista de ventas que se encuentran en el rango de montos especificado.
        """
        inicio = self.validaciones.validar_flotante("Ingrese el monto minimo desde donde quiere iniciar la busqueda:")
        fin = self.validaciones.validar_flotante("Ingresa el monto maximo hasta donde quiere la busqueda:")
        if inicio > fin:
            print("El monto de minimo debe ser menor que el monto maximo.")
            return []

        monto = []
        for venta in ventas:
            if inicio <= venta.get_total() <= fin:
                monto.append(venta)
                return monto



    # 3.GESTION DE CLIENTES///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def registar_cliente (self, clientes):
        """Registra un nuevo cliente en la lista de clientes.

    Argumentos:
    - self: instancia de la clase que contiene el método
    - clientes: lista de clientes registrados en el sistema

    El método solicita al usuario que ingrese el tipo de cliente que desea registrar: si es un 
    cliente jurídico o un cliente natural. Luego, solicita los datos correspondientes al tipo de 
    cliente seleccionado: nombre, cedula, correo, dirección de envío, teléfono para el cliente natural, 
    y razón social, rif, correo, dirección de envío, teléfono para el cliente jurídico.

    Una vez que se han ingresado los datos, se crea una instancia del objeto cliente correspondiente 
    (ClienteNatural o ClienteJuridico) y se agrega a la lista de clientes.

    Finalmente, se guarda la lista actualizada de clientes en un archivo de texto llamado "clientes.txt".

    Este método no devuelve ningún valor.
        """
        while True:
            try:
                tipo_cliente = int(input("""
                Ingrese el tipo de Cliente:
                1.Juridico
                2.Natural
                """))
                if tipo_cliente < 1 or tipo_cliente > 2:
                    raise ValueError
            except:
                print("ERROR: Dato invalido, intente de nuevo")
                continue

            if tipo_cliente == 1: 
                nombre = self.validaciones.validar_alfabetico("Ingrese el nombre del cliente: ")
                cedula = input("Ingrese la cedula del cliente: ")
                correo = input("Ingrese el correo del cliente: ")
                direccion_envio = input("Ingrese la direccion de envio del cliente: ")
                telefono = input("Ingrese el numero de telefono del cliente: ")
                nuevo_cliente = ClienteNatural(nombre, cedula, correo, direccion_envio, telefono)
                clientes.append(nuevo_cliente)
                self.write_txt("clientes.txt", clientes)
            elif tipo_cliente == 2:
                razon = input("Ingrese la razon social del cliente: ")
                rif = input("Ingrese el rif del cliente: ")
                correo = input("Ingrese el correo del cliente: ")
                direccion_envio = input("Ingrese la direccion de envio del cliente: ")
                telefono = input("Ingrese el numero de telefono del cliente: ")
                nuevo_cliente = ClienteJuridico(razon, rif, correo, direccion_envio, telefono)
                clientes.append(nuevo_cliente)
                self.write_txt("clientes.txt", clientes)


    def modificar_cliente(self, clientes): 
        """ Modifica los datos de un cliente existente en la lista de clientes.

    Argumentos:
    - self: instancia de la clase que contiene el método
    - clientes: lista de clientes registrados en el sistema

    El método solicita al usuario que seleccione el tipo de modificación que desea realizar en el cliente:
    nombre o razón social, cédula o rif, correo, dirección de envío o teléfono. Luego, solicita el nombre 
    o razón social del cliente que se desea modificar y muestra una lista de los clientes que coinciden 
    con ese nombre o razón social.

    Para cada tipo de modificación, el método solicita el nuevo valor correspondiente al dato que se desea 
    modificar y actualiza el objeto del cliente seleccionado con los nuevos valores.

    Finalmente, se guarda la lista actualizada de clientes en un archivo de texto llamado "clientes.txt".

    Este método no devuelve ningún valor.
        """
        while True: 
            try:
                m = int(input("""
                Ingrese la opcion de lo que desea modificar:
                1. Nombre o Razon Social
                2. Cedula o Rif
                3. Correo
                4. Direccion de Envio
                5. Telefono
                6. Cliente Completo
                7. Volver al menu
                """)) 

                if m < 1 or m > 7:
                    raise ValueError
            except:
                print("ERROR: Dato invalido, intente de nuevo")
                continue

            if m == 1: #NOMBRE O RAZON SOCIAL
                for cliente in clientes:
                    print(cliente.show())
                cliente_seleccionado = self.validaciones.validar_alfabetico("Indique el nombre o la razon social del cliente que desea modificar: ").capitalize()
                for cliente in clientes:
                    if cliente.isinstance(ClienteNatural) and cliente.get_nombre() == cliente_seleccionado:
                        n_nombre = self.validaciones.validar_alfabetico("Ingrese el nuevo nombre del cliente: ").capitalize()
                        cliente.set_nombre(n_nombre)
                        self.write_txt("clientes.txt", clientes)
                        print("CLIENTE MODIFICADO EXITOSAMENTE!!")
                        print(cliente.show())
                        break
                    if cliente.isinstance(ClienteJuridico) and cliente.get_razon_social() == cliente_seleccionado:
                        n_nombre = self.validaciones.validar_alfabetico("Ingrese la nueva razon social del cliente: ").capitalize()
                        cliente.set_nombre(n_nombre)
                        self.write_txt("clientes.txt", clientes)
                        print("CLIENTE MODIFICADO EXITOSAMENTE!!")
                        print(cliente.show())
                        break

            elif m == 2: #CEDULA O RAZON SOCIAL
                for cliente in clientes:
                    print(cliente.show())
                cliente_seleccionado = self.validaciones.validar_alfabetico("Indique el nombre o la razon social del cliente que desea modificar: ").capitalize()
                for cliente in clientes:
                    if cliente.isinstance(ClienteNatural) and cliente.get_nombre() == cliente_seleccionado:
                        c = input("Ingrese la nueva cedula del cliente: ")
                        cliente.set_cedula(c)
                        self.write_txt("clientes.txt", clientes)
                        print("CLIENTE MODIFICADO EXITOSAMENTE!!")
                        print(cliente.show())
                        break
                    if cliente.isinstance(ClienteJuridico) and cliente.get_razon_social() == cliente_seleccionado:
                        r = input("Ingreseel nuevo rif del cliente: ")
                        cliente.set_rif(r)
                        self.write_txt("clientes.txt", clientes)
                        print("CLIENTE MODIFICADO EXITOSAMENTE!!")
                        print(cliente.show())
                        break

            elif m == 3: #CORREO
                for cliente in clientes:
                    print(cliente.show())
                nombre_cliente_seleccionado = self.validaciones.validar_alfabetico("Indique el nombre del cliente que desea modificar: ").capitalize()
                for cliente in clientes:
                    if cliente.get_nombre() == nombre_cliente_seleccionado:
                        n_correo = input("Ingrese el nuevo correo del cliente: ")
                        cliente.set_correo(n_correo)
                        self.write_txt("clientes.txt", clientes)
                        print("CLIENTE MODIFICADO EXITOSAMENTE!!")
                        print(cliente.show())
                        break

            elif m == 4: #DIRECCION DE ENVIO
                for cliente in clientes:
                    print(cliente.show())
                nombre_cliente_seleccionado = self.validaciones.validar_alfabetico("Indique el nombre del cliente que desea modificar: ").capitalize()
                for cliente in clientes:
                    if cliente.get_nombre() == nombre_cliente_seleccionado:
                        n_direccion_envio = input("Ingrese la nueva direccion de envio del cliente: ")
                        cliente.set_direccion_envio(n_direccion_envio)
                        self.write_txt("clientes.txt", clientes)
                        print("CLIENTE MODIFICADO EXITOSAMENTE!!")
                        print(cliente.show())
                        break

            elif m == 5: #TELEFONO
                for cliente in clientes:
                    print(cliente.show())
                    nombre_cliente_seleccionado = self.validaciones.validar_alfabetico("Indique el nombre del cliente que desea modificar: ").capitalize()
                    n_telf = input("Ingrese el nuevo numero de telefono del cliente: ")
                    for cliente in clientes:
                        if cliente.get_nombre() == nombre_cliente_seleccionado:
                            cliente.set_telf(n_telf)
                            self.write_txt("clientes.txt", clientes)
                            print("CLIENTE MODIFICADO EXITOSAMENTE!!")
                            print(cliente.show())
                    break

            elif m == 6: 
                while True:
                    try:
                        tipo_cliente = int(input("""
                        Ingrese el tipo de Cliente:
                        1.Juridico
                        2.Natural
                        """))
                        if tipo_cliente < 1 or tipo_cliente > 2:
                            raise ValueError
                    except:
                        print("ERROR: Dato invalido, intente de nuevo")
                        continue

                    if tipo_cliente == 1: #JURIDICO
                        for cliente in clientes:
                            print(cliente.show())
                        cliente_seleccionado = input("Indique la razon social del cliente que desea modificar: ")
                        for cliente in clientes:
                            if cliente.get_razon() == cliente_seleccionado:
                                n_razon = input("Ingrese la nueva razon social del cliente: ")
                                n_rif = input("Ingrese el nuevo rif del cliente: ")
                                n_correo = input("Ingrese el nuevo correo del cliente: ")
                                n_direccion_envio = input("Ingrese la nueva direccion de envio del cliente: ")
                                n_telf =  input("Ingrese el nuevo numero de telefono del cliente: ")
                                cliente.set_razon(n_razon)
                                cliente.set_rif(n_rif)
                                cliente.set_correo(n_correo)
                                cliente.set_direccion_envio(n_direccion_envio)
                                cliente.set_telf(n_telf)
                                self.write_txt("clientes.txt", clientes)
                                print("CLIENTE MODIFICADO EXITOSAMENTE!!")
                                print(cliente.show())
                                break

                    elif tipo_cliente == 2: #NATURAL
                        for cliente in clientes:
                            print(cliente.show())
                        nombre_cliente_seleccionado = self.validaciones.validar_alfabetico("Indique el nombre del cliente que desea modificar: ").capitalize()
                        for cliente in clientes:
                            if cliente.get_nombre() == nombre_cliente_seleccionado:
                                n_nombre = self.validaciones.validar_alfabetico("Ingrese el nuevo nombre del cliente: ")
                                n_cedula = input("Ingrese la nueva cedula del cliente: ")
                                n_correo = input("Ingrese el nuevo correo del cliente: ")
                                n_direccion_envio = input("Ingrese la nueva direccion de envio del cliente: ")
                                n_telf =  input("Ingrese el nuevo numero de telefono del cliente: ")
                                cliente.set_nombre(n_nombre)
                                cliente.set_cedula(n_cedula)
                                cliente.set_correo(n_correo)
                                cliente.set_direccion_envio(n_direccion_envio)
                                cliente.set_telf(n_telf)
                                self.write_txt("clientes.txt", clientes)
                                print("CLIENTE MODIFICADO EXITOSAMENTE!!")
                                print(cliente.show())
                                break

            elif m == 7: #VOLVER MENU PRINCIPAL
                break


    def eliminar_cliente(self, clientes):
        """Elimina un cliente existente de la lista de clientes.

    Argumentos:
    - self: instancia de la clase que contiene el método
    - clientes: lista de clientes registrados en el sistema

    El método solicita al usuario que ingrese el nombre o razón social del cliente que desea eliminar. 
    Luego, busca en la lista de clientes el objeto correspondiente al cliente seleccionado y lo elimina 
    de la lista.

    Finalmente, se guarda la lista actualizada de clientes en un archivo de texto llamado "clientes.txt".

    Este método no devuelve ningún valor.
    """
        eliminar = input("Ingrese el nombre o razon social del cliente que desea eliminar: ")
        for cliente in clientes: 
             if cliente.get_nombre()  or cliente.get_razon_social == eliminar:
                clientes.remove(cliente)
                self.write_txt("clientes.txt", clientes)
                print("CLIENTE ELIMINADO EXITOSAMENTE")


    def buscar_cliente_por_cedula(self, clientes):
        """Busca un cliente en la lista de clientes por su número de cédula.

    Argumentos:
    - self: instancia de la clase que contiene el método
    - clientes: lista de clientes registrados en el sistema

    El método solicita al usuario que ingrese el número de cédula del cliente que desea buscar. Luego, busca en 
    la lista de clientes el objeto correspondiente al cliente seleccionado y muestra los detalles del cliente 
    seleccionado.

    Si el número de cédula ingresado no coincide con ningún cliente en la lista, el método no muestra nada.

    Este método no devuelve ningún valor.
        """
        buscar_cliente_cedula = self.validaciones.validar_flotante("Ingrese la cedula del cliente que desea buscar: ")
        for cliente in clientes: 
            if cliente.get_cedula()== buscar_cliente_cedula:
                print(cliente.show())


    def buscar_cliente_por_rif(self, clientes):
        """ Busca un cliente en la lista de clientes por su número de RIF.

    Argumentos:
    - self: instancia de la clase que contiene el método
    - clientes: lista de clientes registrados en el sistema

    El método solicita al usuario que ingrese el número de RIF del cliente que desea buscar. Luego, busca en 
    la lista de clientes el objeto correspondiente al cliente seleccionado y muestra los detalles del cliente 
    seleccionado.

    Si el número de RIF ingresado no coincide con ningún cliente en la lista, el método no muestra nada.

    Este método no devuelve ningún valor.
        """
        buscar_cliente_rif = self.validaciones.validar_flotante("Ingrese el rif del cliente que desea buscar: ")
        for cliente in clientes: 
            if cliente.get_rif()== buscar_cliente_rif:
                print(cliente.show())


    def buscar_cliente_por_correo(self, clientes):
        """ Busca un cliente en la lista de clientes por su dirección de correo electrónico.

    Argumentos:
    - self: instancia de la clase que contiene el método
    - clientes: lista de clientes registrados en el sistema

    El método solicita al usuario que ingrese la dirección de correo electrónico del cliente que desea buscar. 
    Luego, busca en la lista de clientes el objeto correspondiente al cliente seleccionado y muestra los detalles 
    del cliente seleccionado.

    Si la dirección de correo electrónico ingresada no coincide con ningún cliente en la lista, el método no 
    muestra nada.

    Este método no devuelve ningún valor."""
        buscar_cliente_correo = input("Ingrese el correo del cliente que desea buscar: ")
        for cliente in clientes: 
            if cliente.get_correo()== buscar_cliente_correo:
                print(cliente.show())



    # 4.GESTION DE PAGOS/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def registrar_pago(self, pagos, ventas):
        """Registra un pago realizado por un cliente en una venta específica.

    Argumentos:
    - self: instancia de la clase que contiene el método
    - pagos: lista de pagos registrados en el sistema
    - ventas: lista de ventas registradas en el sistema

    El método solicita al usuario que ingrese el RIF del cliente al que desea registrar el pago. Luego, busca 
    en la lista de ventas la venta correspondiente al cliente seleccionado y verifica si el método de envío 
    ha sido registrado. Si el método de envío no ha sido registrado, el método indica que es necesario 
    registrar el envío antes de registrar el pago.

    Luego, el método solicita al usuario que ingrese el tipo de pago, la moneda utilizada y si el pago se 
    realizará al contado. A partir de estos datos, el método calcula el monto total del pago, incluyendo 
    impuestos y descuentos según corresponda.

    Finalmente, el método crea un objeto Pago con la información proporcionada por el usuario y lo agrega a la 
    lista de pagos. Además, actualiza la lista de ventas para registrar el pago correspondiente a la venta 
    seleccionada.

    Si el cliente no se encuentra en la lista de clientes o si no se encuentra ninguna venta correspondiente 
    al cliente seleccionado, el método muestra un mensaje de error.

    Este método no devuelve ningún valor.
    """
        cliente = self.validaciones.validar_flotante("Ingrese el rif del cliente al que desea registar el pago: ")
        aux = False
        for venta in ventas:
            if cliente.isinstance(ClienteJuridico) and cliente.get_rif() == cliente:
                aux = True
                if venta.get_metodo_de_envio() == 'pendiente':
                    print("ES NECESARIO QUE REGISTRE PRIMERO SU ENVIO ANTES DE REGISTRAR EL PAGO YA QUE ESTO HACE VARIAR EL MONTO TOTAL")
                    break
                ops_tipo = input("""
                            Indique el tipo de pago: 
                            1.Punto de Venta
                            2.Pago Movil
                            3.Zelle
                            4.Cash
                            """)
                if ops_tipo == "1":
                    tipo = ("Punto de Venta")
                elif ops_tipo == "2":
                    tipo = ("Pago Movil")
                elif ops_tipo == "3":
                    tipo = ("Zelle")
                elif ops_tipo == "4":
                    tipo = ("Cash")
                try:
                    moneda = int(input("""
                    Indique la moneda del pago: 
                    1.Divisas
                    2.Bolivares
                    """)) 
                    if moneda < 1 or moneda > 2:
                        raise ValueError
                except:
                    print("ERROR: Dato invalido, intente de nuevo")
                    continue
                try:
                    o = int(input("""
                    Pagara al contado?: 
                    1. Si
                    2. No
                    """))
                    if o < 1 or o > 2:
                        raise ValueError
                except:
                    print("ERROR: Dato invalido, intente de nuevo")
                    continue
                subtotal = venta.get_subtotal()
                if o == 1:
                    descuentos = subtotal * 0.05
                elif o == 2:
                    descuentos = 0
                iva = subtotal * 0.16
                if moneda == 1:
                    igtf = subtotal * 0.03
                elif moneda == 2:
                    igtf = 0
                fecha = datetime.date.today()
                costo_servicio = venta.get_envio().get_costo_servicio()
                total = subtotal + iva + igtf + costo_servicio - descuentos
                nuevo_pago = Pago(cliente, total, moneda, tipo, fecha)
                pagos.append(nuevo_pago)
                ventas.set_metodo_de_pago(nuevo_pago)

                self.write_txt("pagos.txt", pagos)
                self.write_txt("ventas.txt", ventas)

                if not aux:
                    print("CLIENTE NO ENCONTRADO")


    def buscar_pago_por_cliente(self, pagos): 
         """ Busca un pago en la lista de pagos por el cliente que realizó el pago.

    Argumentos:
    - self: instancia de la clase que contiene el método
    - pagos: lista de pagos registrados en el sistema

    El método solicita al usuario que seleccione el tipo de cliente (natural o jurídico) y el número de cédula o 
    RIF del cliente correspondiente. Luego, busca en la lista de pagos el objeto correspondiente al cliente 
    seleccionado y muestra los detalles del pago correspondiente.

    Si el número de cédula o RIF ingresado no coincide con ningún cliente en la lista de pagos, el método no 
    muestra nada.

    Este método no devuelve ningún valor.
    """
         while True:
            try:
                tipo_cliente = int(input("""
                    Ingrese el tipo de Cliente:
                    1.Natural
                    2.Juridico
                    """))
                if tipo_cliente < 1 or tipo_cliente > 2:
                        raise ValueError
            except:
                print("ERROR: Dato invalido, intente de nuevo")
                continue
            
            if tipo_cliente == 1:
                buscar_cliente_cedula = self.validaciones.validar_flotante("Ingrese la cedula del cliente del pago que desea buscar: ")
                for pago in pagos: 
                    if pago.get_cedula()== buscar_cliente_cedula:
                        print(pago.show())

            elif tipo_cliente == 2:
                buscar_cliente_rif = self.validaciones.validar_flotante("Ingrese el rif del cliente del pago que desea buscar: ")
                for pago in pagos: 
                    if pago.get_rif()== buscar_cliente_rif:
                        print(pago.show())


    def buscar_pago_por_fecha(self, pagos): 
        """ Busca los pagos realizados dentro de un rango de fechas determinado.

    Argumentos:
    - self: instancia de la clase que contiene el método
    - pagos: lista de pagos registrados en el sistema

    El método solicita al usuario que ingrese dos fechas en formato 'dd/mm/aaaa': una fecha de inicio y una fecha 
    de fin. Luego, busca en la lista de pagos los pagos correspondientes al rango de fechas indicado y devuelve 
    una lista con los objetos correspondientes.

    Si no se encuentra ningún pago dentro del rango de fechas indicado, el método devuelve una lista vacía.

    Este método devuelve una lista con los pagos encontrados.
    
        """
        fecha_inicio = self.validaciones.validar_fecha("Ingresa la fecha desde donde quiere iniciar la busqueda (fecha en formato 'dd/mm/aaaa'):")
        fecha_fin = self.validaciones.validar_fecha("Ingresa la fecha hasta donde quiere la busqueda (fecha en formato 'dd/mm/aaaa'):")
        if fecha_inicio > fecha_fin:
            print("La fecha de inicio debe ser menor o igual que la fecha de fin.")
            return []

        pagos_rango_fechas = []
        for pago in pagos:
            if fecha_inicio <= pago.get_fecha_pago() <= fecha_fin:
                pagos_rango_fechas.append(pago)
                return pagos_rango_fechas


    def buscar_pago_por_tipo_pago(pagos):
        """ Busca los pagos realizados mediante un tipo de pago específico.

    Argumentos:
    - pagos: lista de pagos registrados en el sistema

    El método solicita al usuario que seleccione el tipo de pago que desea buscar (punto de venta, pago móvil, 
    Zelle o Cash). Luego, busca en la lista de pagos los pagos correspondientes al tipo de pago seleccionado y 
    muestra los detalles de los pagos encontrados.

    Si no se encuentra ningún pago correspondiente al tipo de pago seleccionado, el método no muestra nada.

    Este método no devuelve ningún valor.
        """
        try:
            ops_tipo = int(input("""
            Indique el tipo de pago que desea buscar: 
            1.Punto de Venta
            2.Pago Movil
            3.Zelle
            4.Cash
            """))
            if ops_tipo < 1 or ops_tipo > 4:
                raise ValueError
        except:
            print("ERROR: Dato invalido, intente de nuevo")
        if ops_tipo == "1":
            tipo = ("Punto de Venta")
        elif ops_tipo == "2":
            tipo = ("Pago Movil")
        elif ops_tipo == "3":
            tipo = ("Zelle")
        elif ops_tipo == "4":
            tipo = ("Cash")

        for pago in pagos:
            if pago.get_tipo_pago() == tipo:
                print(pago.show())


    def buscar_pago_por_moneda_pagos(self, pagos): 
        """Busca los pagos realizados en una moneda específica.

    Argumentos:
    - self: instancia de la clase que contiene el método
    - pagos: lista de pagos registrados en el sistema

    El método solicita al usuario que seleccione la moneda en la que se realizó el pago que desea buscar (divisas 
    o bolívares). Luego, busca en la lista de pagos los pagos correspondientes a la moneda seleccionada y muestra 
    los detalles de los pagos encontrados.

    Si no se encuentra ningún pago correspondiente a la moneda seleccionada, el método no muestra nada.

    Este método no devuelve ningún valor.
        """
        try:
            moneda = int(input("""
            Indique la moneda del pago que desea buscar: 
            1.Divisas
            2.Bolivares
            """)) 
            if moneda < 1 or moneda > 2:
                raise ValueError
        except:
            print("ERROR: Dato invalido, intente de nuevo")
        if moneda == 1:
            m = ('divisas')
        elif moneda == 2:
            m = ('bolivares')

        for pago in pagos:
            if pago.get_moneda_pago() == m:
                print(pago.show())


    # 5.GESTION DE ENVIOS//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def registra_envio(self, envios, ventas):
        """Registra un envío para una venta y lo agrega a la lista de envíos.

    Argumentos:
    - self: instancia de la clase que contiene el método
    - envios: lista de envíos registrados en el sistema
    - ventas: lista de ventas registradas en el sistema

    El método solicita al usuario el RIF del cliente al que se le desea registrar el envío. Si el cliente es 
    encontrado, se crea una nueva orden de compra con el cliente, el carrito de compras y el tipo de pago de la 
    última venta realizada por el cliente.

    Luego, se solicita al usuario que seleccione el servicio de envío (MRW, Zoom o Delivery) y se crea un objeto 
    Envio con la orden de compra, el servicio de envío seleccionado, el costo del servicio, la fecha actual y, 
    en caso de haber seleccionado Delivery, los datos del motorizado.

    El objeto Envio se agrega a la lista de envíos y se actualizan las ventas correspondientes con el método de 
    envío seleccionado.

    Este método no devuelve ningún valor.
        """
        cliente = self.validaciones.validar_flotante("Ingrese el rif del cliente al que desea registar el envio: ")
        aux = False
        for venta in ventas:
            if cliente.isinstance(ClienteJuridico) and cliente.get_rif() == cliente:
                aux = True

            if not aux:
                    print("CLIENTE NO ENCONTRADO")

        try:
            met_pago =  int(input("""
            Indique el tipo de pago: 
            1.Punto de Venta
            2.Pago Movil
            3.Zelle
            4.Cash
            """))
            if met_pago < 1 or met_pago > 2:
                raise ValueError
        except:
            print("ERROR: Dato invalido, intente de nuevo")
        if met_pago == "1":
            tipo = ("Punto de Venta")
        elif met_pago == "2":
            tipo = ("Pago Movil")
        elif met_pago == "3":
            tipo = ("Zelle")
        elif met_pago == "4":
            tipo = ("Cash")
        for venta in ventas:
            cliente = venta.get_cliente()
            carrito = venta.get_carrito()
        noc = OrdenCompra(cliente, carrito, tipo)
        
        while True:
            try:
                ops_envio = int(input("""
                Seleccione el servicio de envio: 
                1. MRW 5$
                2. Zoom 7$
                3. Delivery 10$
                """))
                if ops_envio < 1 or ops_envio > 3:
                    raise ValueError
            except:
                print("ERROR: Dato invalido, intente de nuevo")
                continue
            if ops_envio == "1":
                envio = ("MRW")
                costo_servicio = 5
                motorizado = None
            elif ops_envio == "2":
                envio = ("Zoom")
                costo_servicio = 7
                motorizado = None
            elif ops_envio == "3":
                envio = ("Delivery")
                costo_servicio = 10
                nombre = input("Ingrese el nombre del motorizado del delivery: ")
                telf = input("Ingrese el telefono del delivery: ")
                motorizado = Motorizado(nombre, telf)
            fecha = datetime.date.today()
            envio = Envio(noc, envio, motorizado, costo_servicio, fecha)
            envios.append(envio)
            for venta in ventas:
                venta.set_metodo_de_envio(envio)

            self.write_txt("envios.txt", envios)
            self.write_txt("ventas.txt", ventas)


    def buscar_envio_por_cliente(self, envios): 
        """Busca los envíos realizados para un cliente específico.

    Argumentos:
    - self: instancia de la clase que contiene el método
    - envios: lista de envíos registrados en el sistema

    El método solicita al usuario que ingrese el nombre o razón social del cliente para el cual desea buscar envíos. 
    Luego, busca en la lista de envíos los envíos correspondientes al cliente indicado y muestra los detalles de los 
    envíos encontrados.

    Si no se encuentra ningún envío correspondiente al cliente indicado, el método no muestra nada.

    Este método no devuelve ningún valor.
        """
        cliente = input("Ingrese el nombre o razon social  del cliente del envio que desea buscar: ")
        for envio in envios:
            if envio.get_cliente() or envio.get_razon_social()== cliente:
                print(envio.show())

    def buscar_envio_por_fecha(self, envios): 
        """ Busca los envíos realizados en un rango de fechas específico.

    Argumentos:
    - self: instancia de la clase que contiene el método
    - envios: lista de envíos registrados en el sistema

    El método solicita al usuario que ingrese la fecha desde donde quiere iniciar la búsqueda y la fecha hasta 
    donde quiere la búsqueda. Luego, busca en la lista de envíos los envíos correspondientes al rango de fechas 
    indicado y muestra los detalles de los envíos encontrados.

    Si no se encuentra ningún envío correspondiente al rango de fechas indicado, el método no muestra nada.

    El formato de las fechas debe ser dd/mm/aaaa.

    Este método no devuelve ningún valor.
        """
        fecha_inicio = self.validaciones.validar_fecha("Ingresa la fecha desde donde quiere iniciar la busqueda (fecha en formato 'dd/mm/aaaa'):")
        fecha_fin = self.validaciones.validar_fecha("Ingresa la fecha hasta donde quiere la busqueda (fecha en formato 'dd/mm/aaaa'):")
        if fecha_inicio > fecha_fin:
            print("La fecha de inicio debe ser menor o igual que la fecha de fin.")
            return []

        envios_rango_fechas = []
        for envio in envios:
            if fecha_inicio <= envio.get_fecha_envio() <= fecha_fin:
                envios_rango_fechas.append(envio)
                return envios_rango_fechas



    # 6.INDICADORES DE GESTION (ESTADISTICAS)////////////////////////////////////////////////////////////////////////////////////////////////////

    def generar_informes_ventas(self, ventas):
        """Genera diferentes informes relacionados con las ventas realizadas.

    Argumentos:
    - self: instancia de la clase que contiene el método
    - ventas: lista de ventas registradas en el sistema

    El método presenta al usuario un menú para seleccionar el tipo de informe que desea generar. Los informes 
    disponibles son:

    1. Ventas totales por día, semana, mes y año.
    2. Productos más vendidos.
    3. Clientes más frecuentes.
    4. Volver al menú de Gestión de Estadísticas.

    Si el usuario selecciona una opción válida, el método procesa los datos necesarios para generar el informe 
    correspondiente y lo muestra en pantalla.

    Si el usuario selecciona la opción 4, el método sale del bucle y vuelve al menú de Gestión de Estadísticas.

    Este método no devuelve ningún valor.
        """
        while True:
            print("GENERAR INFORMES DE VENTAS")
            try: 
                v = int(input("""
                1. Ventas totales por día, semana, mes y año
                2. Productos más vendidos
                3. Clientes más frecuentes
                4. Volver al menu de Gestion de Estadisticas
                """))
                if v < 1 or v > 4:
                    raise ValueError
            except:
                print("ERROR: Dato invalido, intente de nuevo")
                continue
        
            if v == 1: # Ventas totales por día, semana, mes y año
                ventas_por_dia = {venta["fecha"]: venta["precio"] * venta["cantidad"] for venta in ventas}
                ventas_por_semana = {}
                ventas_por_mes = {}
                ventas_por_anio = {}

                for fecha_str, monto in ventas_por_dia.items():
                    fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
                    semana = fecha.strftime('%Y-%U')
                    mes = fecha.strftime('%Y-%m')
                    anio = fecha.strftime('%Y')
                    ventas_por_semana[semana] = ventas_por_semana.get(semana, 0) + monto
                    ventas_por_mes[mes] = ventas_por_mes.get(mes, 0) + monto
                    ventas_por_anio[anio] = ventas_por_anio.get(anio, 0) + monto

                print("Ventas totales por día:")
                print(ventas_por_dia)
                print("Ventas totales por semana:")
                print(ventas_por_semana)
                print("Ventas totales por mes:")
                print(ventas_por_mes)
                print("Ventas totales por año:")
                print(ventas_por_anio)

            elif v == 2:# Productos más vendidos
                productos_vendidos = [venta["producto"] for venta in ventas]
                productos_vendidos_counter = Counter(productos_vendidos)
                productos_mas_vendidos = productos_vendidos_counter.most_common(3)

                print("Productos más vendidos:")
                for producto, cantidad in productos_mas_vendidos:
                    print(f"{producto}: {cantidad} ventas")

            elif v == 3:# Clientes más frecuentes
                clientes_frecuentes = [venta["cliente"] for venta in ventas]
                clientes_frecuentes_counter = Counter(clientes_frecuentes)
                clientes_mas_frecuentes = clientes_frecuentes_counter.most_common(3)

                print("Clientes más frecuentes:")
                for cliente, cantidad in clientes_mas_frecuentes:
                    print(f"{cliente}: {cantidad} compras")

            elif v == 4: #Salir
                break

    def generar_informes_pagos(self, pagos, ventas):
        """Genera diferentes informes relacionados con los pagos realizados.

    Argumentos:
    - self: instancia de la clase que contiene el método
    - pagos: lista de pagos registrados en el sistema
    - ventas: lista de ventas registradas en el sistema

    El método presenta al usuario un menú para seleccionar el tipo de informe que desea generar. Los informes 
    disponibles son:

    1. Pagos totales por día, semana, mes y año.
    2. Clientes con pagos pendientes.
    3. Volver al menú de Gestión de Estadísticas.

    Si el usuario selecciona una opción válida, el método procesa los datos necesarios para generar el informe 
    correspondiente y lo muestra en pantalla.

    Si el usuario selecciona la opción 3, el método sale del bucle y vuelve al menú de Gestión de Estadísticas.

    Este método no devuelve ningún valor.
        """
        while True:
            print("GENERAR INFORMES DE PAGOS")
            try: 
                v = int(input("""
                1. Pagos totales por día, semana, mes y año
                2. Clientes con pagos pendientes
                3. Volver al menu de Gestion de Estadisticas
                """))
                if v < 1 or v > 3:
                    raise ValueError
            except:
                print("ERROR: Dato invalido, intente de nuevo")
                continue

            if v == 1:# Pagos totales por día, semana, mes y año
                pagos_por_dia = {pago["fecha"]: pago["monto"] for pago in pagos}
                pagos_por_semana = {}
                pagos_por_mes = {}
                pagos_por_anio = {}

                for fecha_str, monto in pagos_por_dia.items():
                    fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
                    semana = fecha.strftime('%Y-%U')
                    mes = fecha.strftime('%Y-%m')
                    anio = fecha.strftime('%Y')
                    pagos_por_semana[semana] = pagos_por_semana.get(semana, 0) + monto
                    pagos_por_mes[mes] = pagos_por_mes.get(mes, 0) + monto
                    pagos_por_anio[anio] = pagos_por_anio.get(anio, 0) + monto

                print("Pagos totales por día:")
                print(pagos_por_dia)
                print("Pagos totales por semana:")
                print(pagos_por_semana)
                print("Pagos totales por mes:")
                print(pagos_por_mes)
                print("Pagos totales por año:")
                print(pagos_por_anio)

            elif v == 2: # Clientes con pagos pendientes
                clientes_con_pendientes = set([pago["cliente"] for pago in pagos if pago["estado"] == "pendiente"])

                print("Clientes con pagos pendientes:")
                for cliente in clientes_con_pendientes:
                    pagos_pendientes = [venta for venta in ventas if venta["cliente"] == cliente and venta["metodo_de_pago"] == "pendiente"]
                    total_pendiente = sum(pago["monto"] for pago in pagos_pendientes)
                    print(f"{cliente}: ${total_pendiente:.2f} pendientes")

            elif v == 3: #Volver al menu gestion de estadisticas
                break


    def generar_informes_envios(self, envios):
        """Genera diferentes informes relacionados con los envíos realizados.

    Argumentos:
    - self: instancia de la clase que contiene el método
    - envios: lista de envíos registrados en el sistema

    El método presenta al usuario un menú para seleccionar el tipo de informe que desea generar. Los informes 
    disponibles son:

    1. Envíos totales por día, semana, mes y año.
    2. Productos más enviados.
    3. Clientes con envíos pendientes.
    4. Volver al menú de Gestión de Estadísticas.

    Si el usuario selecciona una opción válida, el método procesa los datos necesarios para generar el informe 
    correspondiente y lo muestra en pantalla.

    Si el usuario selecciona la opción 4, el método sale del bucle y vuelve al menú de Gestión de Estadísticas.

    Este método no devuelve ningún valor.
        """
        while True:
            print("GENERAR INFORMES DE ENVIOS")
            try: 
                v = int(input("""
                1.Envíos totales por día, semana, mes y año
                2.Productos más enviados
                3.Clientes con envíos pendientes
                4.Volver al menu Gestion de Estadisticas
                """))
                if v < 1 or v > 4:
                    raise ValueError
            except:
                print("ERROR: Dato invalido, intente de nuevo")
                continue
            
            if v == 1: #ENVIOS TOTALES
                while True:
                    print("GENERAR INFORMES DE ENVIOS")
                    try: 
                        x = int(input("""
                        1.Envíos totales por día
                        2.Envíos totales por semana
                        3.Envíos totales por mes 
                        4.Envíos totales por anio
                        5..Volver al menu Informes Envios
                        """))
                        if x < 1 or x > 5:
                            raise ValueError
                    except:
                        print("ERROR: Dato invalido, intente de nuevo")
                        continue
                    if x == 1: #ENVIOS TOTALES POR DIA
                        envios_por_dia = {}
                        for envio in envios:
                            fecha = datetime.strptime(envio['fecha'], '%Y-%m-%d')
                            dia = fecha.strftime('%Y-%m-%d')
                            envios_por_dia[dia] = envios_por_dia.get(dia, 0) + 1
                        for dia, envios in envios_por_dia.items():
                            print(f"Fecha: {dia}, Envíos: {envios}")
                    elif x == 2: #ENVIOS TOTALES POR SEMANA
                        envios_por_semana = {}
                        for envio in envios:
                            fecha = datetime.strptime(envio['fecha'], '%Y-%m-%d')
                            semana = fecha.strftime('%Y-%W')
                            envios_por_semana[semana] = envios_por_semana.get(semana, 0) + 1
                        for semana, envios in envios_por_semana.items():
                            print(f"Semana: {semana}, Envíos: {envios}")
                    elif x == 3: #ENVIOS TOTALES POR MES
                        envios_por_mes = {}
                        for envio in envios:
                            fecha = datetime.strptime(envio['fecha'], '%Y-%m-%d')
                            mes = fecha.strftime('%Y-%m')
                            envios_por_mes[mes] = envios_por_mes.get(mes, 0) + 1
                        for mes, envios in envios_por_mes.items():
                            print(f"Mes: {mes}, Envíos: {envios}")
                    elif x == 4: #ENVIOS TOTALES POR ANIO
                        envios_por_anio = {}
                        for envio in envios:
                            fecha = datetime.strptime(envio['fecha'], '%Y-%m-%d')
                            anio = fecha.strftime('%Y')
                            envios_por_anio[anio] = envios_por_anio.get(anio, 0) + 1
                        for anio, envios in envios_por_anio.items():
                            print(f"Año: {anio}, Envíos: {envios}")
                    elif x == 5: #SALIDA
                        pass

            elif v == 2: #PRODUCTOS MAS VENDIDOS
                productos = [envio['producto'] for envio in envios]
                productos_mas_enviados = sorted(set(productos), key=productos.count, reverse=True)
                for producto in productos_mas_enviados:
                    envios = productos.count(producto)
                    print(f"Producto: {producto}, Envíos: {envios}")

            elif v == 3: #CLIENTES CON ENVIOS PENDIENTES
                clientes = set([envio['cliente'] for envio in filter(lambda x: x['estado'] == 'pendiente', envios)])
                for cliente in clientes:
                    print(f"Cliente: {cliente}")
                                
            elif v == 4: #VOLVER AL MENU INFORMES VENTAS
                break
