import typing 

class Venta:
    def __init__(self, cliente : str, carrito : list[{str,int}], metodo_de_pago : str, metodo_de_envio : str, subtotal : float, descuentos : float, IVA :float, IGTF : float, total : float):
        self.__cliente = cliente
        self.__carrito = carrito
        self.__metodo_de_pago = metodo_de_pago
        self.__metodo_de_envio = metodo_de_envio
        self.__subtotal = subtotal
        self.__descuentos = descuentos
        self.__IVA = IVA
        self.__IGTF = IGTF
        self.__total = total

    def set_cliente(self, cliente):
        self.__cliente = cliente

    def get_cliente(self):
        return self.__cliente
    
    def set_carrito(self, carrito):
        self.__carrito= carrito

    def get_carrito(self):
        return self.__carrito
    
    def set_metodo_de_pago(self, metodo_de_pago):
        self.__metodo_de_pago= metodo_de_pago

    def get_metodo_de_pago(self):
        return self.__metodo_de_pago
    
    def set_metodo_de_envio(self, metodo_de_envio):
        self.__metodo_de_envio= metodo_de_envio

    def get_metodo_de_envio(self):
        return self.__metodo_de_envio
    
    def set_subtotal(self, subtotal):
        self.__subtotal = subtotal

    def get_subtotal(self):
        return self.__subtotal
    
    def set_descuentos(self, descuentos):
        self.__descuentos= descuentos

    def get_descuentos(self):
        return self.__descuentos
    
    def set_IVA(self, IVA):
        self.__IVA= IVA

    def get_IVA(self):
        return self.__IVA
    
    def set_IGTF(self, IGTF):
        self.__IGTF= IGTF

    def get_IGTF(self):
        return self.__IGTF
    
    def set_total(self, total):
        self.__total= total

    def get_total(self):
        return self.__total

    def show(self):
        return f"""
        Clientes:{self.__clientes}
        productos Comprados:{self.__productos_comprados}
        cantidad de Cada Producto:{self.__cantidad_de_cada_producto}
        Metodo de Pago:{self.__metodo_de_pago}
        Metodo de Envio:{self.__metodo_de_envio}
        Subtotal:{self.__subtotal}
        Descuentos:{self.__descuentos}
        IVA:{self.__IVA}
        IGTF:{self.__IGTF}
        Total:{self.__total}
        """