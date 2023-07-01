import typing
from Cliente import Cliente

class ClienteNatural(Cliente):
    def __init__(self, nombre : str, cedula : str, correo : str, direccion_envio : str, telf : str):
        self.__nombre = nombre
        self.__cedula = cedula
        super().__init__(correo, direccion_envio, telf)

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre
    
    def set_cedula(self, cedula):
        self.__cedula = cedula

    def get_cedula(self):
        return self.__cedula
    

    def show(self):
        return f"""
        Nombre: {self.__nombre}
        Cedula: {self.__cedula}
        Correo: {self.__correo}
        Direccion_envio: {self.__direccion_envio}
        Telf: {self.__telf}
        """
    
    