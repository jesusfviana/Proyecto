import typing
from Cliente import Cliente

class ClienteJuridico(Cliente):
    def __init__(self, razon_social : str, rif : str, correo : str, direccion_envio : str, telf : str):
        self.__razon_social = razon_social
        self.__rif = rif
        super().__init__(correo, direccion_envio, telf)

    def set_razon_social(self, razon_social):
        self.__razon_social = razon_social

    def get_razon_social(self):
        return self.__razon_social
    
    def set_rif(self, rif):
        self.__rif = rif

    def get_rif(self):
        return self.__rif
    

    def show(self):
        return f"""
        Razon Social: {self.__razon_social}
        rif: {self.__rif}
        Correo: {self.__correo}
        Direccion_envio: {self.__direccion_envio}
        Telf: {self.__telf}
        """