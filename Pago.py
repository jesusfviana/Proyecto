import typing

class Pago:
    def __init__(self, cliente : str, monto : float, moneda_pago : str, tipo_pago : str, fecha_pago : str):
        self.__cliente = cliente 
        self.__monto = monto
        self.__moneda_pago = moneda_pago
        self.__tpo_pago = tipo_pago
        self.__fecha_pago = fecha_pago

    def set_cliente(self, cliente):
        self.__cliente = cliente

    def get_cliente(self):
        return self.__cliente
    
    def set_monto(self, monto):
        self.__monto = monto

    def get_monto(self):
        return self.__monto

    def set_moneda_pago(self, moneda_pago):
        self.__moneda_pago = moneda_pago

    def get_moneda_pago(self):
        return self.__moneda_pago
    
    def set_tipo_pago(self, tipo_pago):
        self.__tipo_pago = tipo_pago

    def get_tipo_pago(self):
        return self.__tipo_pago
    
    def set_fecha_pago(self, fecha_pago):
        self.__fecha_pago = fecha_pago

    def get_fecha_pago(self):
        return self.__fecha_pago
    
    def show(self):
        return f"""
        Cliente : {self.__cliente}
        Monto Pago: {self.__monto_pago}
        Moneda Pago: {self.__moneda_pago}
        Tipo Pago: {self.__tpo_pago}
        Fecha Pago: {self.__fecha_pago}
        """

    