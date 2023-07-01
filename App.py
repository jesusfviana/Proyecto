from Funciones import Funciones
from Producto import Producto
import requests, json

class App:
    
    def __init__(self):
        """Inicializa una instancia de la clase Tienda con las siguientes propiedades:
    - funciones: instancia de la clase Funciones, que contiene algunas funciones útiles para la tienda.
    - productos: lista vacía para almacenar los productos disponibles en la tienda.
    - ventas: lista vacía para almacenar las ventas realizadas en la tienda.
    - pagos: lista vacía para almacenar los pagos registrados en la tienda.
    - envios: lista vacía para almacenar los envíos realizados en la tienda.
    - clientes: lista vacía para almacenar los clientes registrados en la tienda.

    Este método no recibe argumentos y no devuelve ningún valor.
        """
        self.funciones = Funciones()
        self.productos = []
        self.ventas = []
        self.pagos = []
        self.envios = []
        self.clientes = []

    def load_data(self):
        """Carga los datos de los productos disponibles en la tienda desde una fuente externa y los almacena en una lista.
    Además, guarda la lista de productos en un archivo de texto para su posterior uso.

    Este método no recibe argumentos y no devuelve ningún valor._summary_
        """
        response = requests.request("GET", 'https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/main/products.json').json()

        for i in range(0,len(response)):
            producto=response
            nombre=producto[i]['name']
            descripcion=producto[i]['description']
            precio=producto[i]['price']
            categoria=producto[i]['category']
            inventario = producto[i]['quantity']
            p = Producto(nombre, descripcion, precio, categoria, inventario)
            self.productos.append(p)
        
        self.funciones.write_txt("productos.txt", self.productos)

    def start(self):
        """ Inicia la aplicación cargando los datos de los productos disponibles en la tienda y los datos de clientes, ventas, 
    pagos y envíos previamente almacenados en archivos de texto.
    Los datos de clientes, ventas, pagos y envíos se cargan en las respectivas listas de la instancia de la clase Tienda.

    Este método no recibe argumentos y no devuelve ningún valor.
        """
        self.load_data()
        self.funciones.read_txt("clientes.txt", self.clientes)
        self.funciones.read_txt("ventas.txt", self.ventas)
        self.funciones.read_txt("pagos.txt", self.pagos)
        self.funciones.read_txt("envios.txt", self.envios)
        while True:
            print("/////////////////////////////////////////BIENVENIDO A TIENDA DE PRODUCTOS NATURALES/////////////////////////////////////////")
            while True:
                try:
                    menu = int(input("""
                    Ingrese un numero segun la accion que desee realizar:
                    1.Gestión de Productos
                    2.Gestión de Ventas
                    3.Gestión de Clientes
                    4.Gestión de Pagos
                    5.Gestión de Envíos
                    6.Indicadores de Gestión (Estadísticas)
                    7.Salir
                    """))
                    if menu < 1 or menu > 8:
                        raise ValueError
                    break
                except:
                    print("ERROR: Dato invalido, intente de nuevo")
                    continue

            # 1.GESTION DE PRODUCTOS
            if menu == 1:
                while True:
                    print("/////////////////////////////////////////GESTION DE PRODUCTOS/////////////////////////////////////////")
                    try:
                        menu_gestion_productos = int(input("""
                        1. Agregar Productos
                        2. Buscar Productos
                        3. Modificar la Informacion de Productos Existentes 
                        4. Eliminar Productos de la Tienda
                        5. Volver al Menu de la Tienda
                        """))
                        if menu_gestion_productos < 1 or menu_gestion_productos > 5:
                            raise ValueError
                        break
                    except:
                        print("ERROR: Dato invalido, intente de nuevo")
                        continue

                if menu_gestion_productos == 1:
                    nuevo_producto = self.funciones.agregar_producto(self.productos)
                    self.productos.append(nuevo_producto)

                elif menu_gestion_productos == 2:
                    while True: 
                        print("Buscar productos en función de los siguientes filtros: ")
                        try:
                            menu_busqueda_productos = int(input("""
                            1. Categoría
                            2. Precio
                            3. Nombre
                            4. Disponibilidad en Inventario
                            5. Volver al Menu Gestion de Productos
                            """))

                            if menu_busqueda_productos < 1 or menu_busqueda_productos > 5:
                                raise ValueError
                        except:
                            print("ERROR: Dato invalido, intente de nuevo")
                            continue
                        
                        if menu_busqueda_productos == 1:
                            self.funciones.buscar_productos_por_categoria(self.productos)
                        elif menu_busqueda_productos == 2:
                            self.funciones.buscar_productos_por_precio(self.productos)
                        elif menu_busqueda_productos == 3:
                            self.funciones.buscar_productos_por_nombre(self.productos)
                        elif menu_busqueda_productos == 4:
                            self.funciones.buscar_productos_por_disponibilidad_en_inventario(self.productos)
                        elif menu_busqueda_productos == 5:
                            break

                elif menu_gestion_productos == 3:
                    self.funciones.modificar_producto(self.productos)
                elif menu_gestion_productos == 4:
                    self.funciones.eliminar_productos(self.productos)
                elif menu_gestion_productos == 5:
                    break
            

            # 2.GESTION DE VENTAS
            elif menu == 2:
                while True:
                    print("/////////////////////////////////////////GESTION DE VENTAS/////////////////////////////////////////")
                    try:
                        menu_gestion_ventas = int(input("""
                        1. Registrar Ventas
                        2. Buscar Ventas
                        3. Volver al Menu de la Tienda
                        """))

                        if menu_gestion_ventas < 1 or menu_gestion_ventas > 3:
                            raise ValueError
                        
                    except:
                        print("ERROR: Dato invalido, intente de nuevo")
                        continue

                    if menu_gestion_ventas == 1:
                        self.funciones.registro_ventas(self.ventas, self.envios, self.clientes, self.pagos, self.productos)
                    elif menu_gestion_ventas == 2:
                        while True: 
                            print("Buscar ventas en función de los siguientes filtros: ")
                            try:
                                menu_busqueda_ventas = int(input("""
                                1. Cliente
                                2. Fecha
                                3. Monto Total
                                4. Volver al Menu Gestion de Ventas
                                """))

                                if menu_busqueda_ventas < 1 or menu_busqueda_ventas > 4:
                                    raise ValueError
                            except:
                                print("ERROR: Dato invalido, intente de nuevo")
                                continue
                            
                            if menu_busqueda_ventas == 1:
                                self.funciones.buscar_venta_por_cliente(self.ventas)
                            elif menu_busqueda_ventas == 2:
                                self.funciones.buscar_venta_por_fecha(self.ventas)
                            elif menu_busqueda_ventas == 3:
                                self.funciones.buscar_venta_por_monto_total(self.ventas)
                            elif menu_busqueda_ventas == 4:
                                break
                    elif menu_gestion_ventas == 3:
                        break


            # 3.GESTION DE CLIENTES
            elif menu == 3:
                while True:
                    print("/////////////////////////////////////////GESTION DE CLIENTES/////////////////////////////////////////")
                    try:
                        menu_gestion_clientes = int(input("""
                        1. Registrar Clientes
                        2. Modificar Clientes
                        3. Eliminar Clientes
                        4. Buscar Clientes
                        5. Volver al Menu de la Tienda
                        """))

                        if menu_gestion_clientes < 1 or menu_gestion_clientes > 5:
                            raise ValueError
                        
                    except:
                        print("ERROR: Dato invalido, intente de nuevo")
                        continue
                    
                    if menu_gestion_clientes == 1:
                        self.funciones.registar_cliente(self.clientes)
                    elif menu_gestion_clientes == 2:
                        self.funciones.modificar_cliente(self.clientes)
                    elif menu_gestion_clientes == 3:
                        self.funciones.eliminar_cliente(self.clientes)
                    elif menu_gestion_clientes == 4:
                        while True: 
                            print("Buscar clientes en función de los siguientes filtros: ")
                            try:
                                menu_busqueda_clientes = int(input("""
                                1. Cedula
                                2. Rif
                                3. Correo
                                4. Volver al Menu Gestion de Clientes
                                """))

                                if menu_busqueda_clientes < 1 or menu_busqueda_clientes > 4:
                                    raise ValueError
                            except:
                                print("ERROR: Dato invalido, intente de nuevo")
                                continue
                            if menu_busqueda_clientes == 1:
                                self.funciones.buscar_cliente_por_cedula(self.clientes)
                            elif menu_busqueda_clientes == 2:
                                self.funciones.buscar_cliente_por_rif(self.clientes)
                            elif menu_busqueda_clientes == 3:
                                self.funciones.buscar_cliente_por_correo(self.clientes)
                            elif menu_busqueda_clientes == 4:
                                break
                    elif menu_gestion_clientes == 5:
                        break


            # 4.GESTION DE PAGOS
            elif menu == 4:
                while True:
                    print("/////////////////////////////////////////GESTION DE PAGOS/////////////////////////////////////////")
                    try:
                        menu_gestion_pagos = int(input("""
                        1. Registrar Pagos
                        2. Buscar Pagos
                        3. Volver al Menu de la Tienda
                        """))

                        if menu_gestion_pagos < 1 or menu_gestion_pagos > 3:
                            raise ValueError
                        
                    except:
                        print("ERROR: Dato invalido, intente de nuevo")
                        continue

                    if menu_gestion_pagos == 1:
                        self.funciones.registrar_pago(self.pagos)
                    elif menu_gestion_pagos == 2:
                        buscar_pagos = input("""
                        Seleccione el tipo de busqueda:
                        1.Buscar por cliente
                        2.Buscar por fecha
                        3.Buscar por tipo de pago
                        4.Buscar por moneda de pago
                        5.Volver al menu de gestion de pagos
                        """)
                        if buscar_pagos == "1":
                            self.funciones.buscar_pago_por_cliente(self.pagos)
                        elif buscar_pagos == "2":
                            self.funciones.buscar_pago_por_fecha(self.pagos)
                        elif buscar_pagos == "3":
                            self.funciones.buscar_pago_por_tipo_pago(self.pagos)
                        elif buscar_pagos == "4":
                            self.funciones.buscar_pago_por_moneda_pago(self.pagos)
                        elif buscar_pagos == "5":
                            break
                    elif menu_gestion_pagos == 3:
                        break


            # 5.GESTION DE ENVIOS
            elif menu == 5:
                while True:
                    print("/////////////////////////////////////////GESTION DE ENVIOS/////////////////////////////////////////")
                    try:
                        menu_gestion_envios = int(input("""
                        1. Registrar Envios
                        2. Buscar Envios
                        3. Volver al Menu de la Tienda
                        """))

                        if menu_gestion_envios < 1 or menu_gestion_envios > 3:
                            raise ValueError
                        
                    except:
                        print("ERROR: Dato invalido, intente de nuevo")
                        continue

                    if menu_gestion_envios == 1:
                        self.funciones.registra_envio(self.envios)
                    elif menu_gestion_envios == 2:
                        buscar_envios = input("""
                        Indique el tipo de busqueda:
                        1.Cliente
                        2.Fecha
                        3.Volver al menu de gestion de envios
                        """)
                        if buscar_envios == "1":
                            self.funciones.buscar_envio_por_cliente(self.envios)
                        elif buscar_envios == "2":
                            self.funciones.buscar_envio_por_fecha(self.envios)
                        elif buscar_envios == "3":
                            break
                    elif menu_gestion_envios == 3:
                        break


            # 6.INDICADORES DE GESTION (ESTADISTICAS)
            elif menu == 6:
                while True:
                    print("/////////////////////////////////////////INDICADORES DE GESTION (ESTADISTICA)/////////////////////////////////////////")
                    try:
                        menu_gestion_estadisticas = int(input("""
                        1. Generar Informes de Ventas
                        2. Generar Informes de Pagos
                        3. Generar Informes de Envios
                        4. Volver al Menu de la Tienda
                        """))

                        if menu_gestion_estadisticas < 1 or menu_gestion_estadisticas > 4:
                            raise ValueError
                        
                    except:
                        print("ERROR: Dato invalido, intente de nuevo")
                        continue

                    if menu_gestion_estadisticas == 1:
                        self.funciones.generar_informes_ventas(self.ventas)
                    elif menu_gestion_estadisticas == 2:
                        self.funciones.generar_informes_pagos(self.pagos, self.ventas)
                    elif menu_gestion_estadisticas == 3:
                        self.funciones.generar_informes_envios(self.envios)
                    elif menu_gestion_estadisticas == 4:
                        break


            # 7.SALIR
            elif menu == 7:
                print("SALIDA EXITOSA!!")
                break

