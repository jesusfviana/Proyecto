import typing

class Cliente:
    def __init__(self, nombre : str, cedula : str, correo : str, direccion_envio : str, telf : str):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__correo = correo
        self.__direccion_envio = direccion_envio
        self.__telf = telf

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre
    
    def set_cedula(self, cedula):
        self.__cedula = cedula

    def get_cedula(self):
        return self.__cedula
    
    def set_correo(self, correo):
        self.__correo = correo

    def get_correo(self):
        return self.__correo
    
    def set_direccion_envio(self, direccion_envio):
        self.__direccion_envio = direccion_envio

    def get_direccion_envio(self):
        return self.__direccion_envio
    
    def set_telf(self, telf):
        self.__telf = telf

    def get_telf(self):
        return self.__telf

    def show(self):
        return f"""
        Razon Social: {self.__razon_social}
        Cedula: {self.__cedula}
        Correo: {self.__correo}
        Direccion_envio: {self.__direccion_envio}
        Telf: {self.__telf}
        """