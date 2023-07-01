import typing

class OrdenCompra:
    def __init__(self, cliente : str, carrito : list[{str, int}],  metodo_de_pago : str):
        self.__cliente = cliente
        self.__carrito = carrito
        self.__metodo_de_pago = metodo_de_pago

    def set_cliente(self, cliente):
        self.__cliente == cliente
    
    def get_cliente(self):
        return self.__cliente
    
    def set_carrito(self, carrito):
        self.__carrito = carrito

    def get_carrito(self, carrito):
        return self.__carrito

    def set_metodo_de_pago(self, metodo_de_pago):
        self.__metodo_de_pago= metodo_de_pago

    def get_metodo_de_pago(self):
        return self.__metodo_de_pago

    def show(self):
        return f"""
        Cliente:{self.__cliente}
        carrito:{self.__carrito}
        Metodo de Pago:{self.__metodo_de_pago}
        """