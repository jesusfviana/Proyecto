import typing

class Motorizado:
    def __init__(self, nombre : str, telf : str):
        self.__nombre = nombre
        self.__tefl = telf

    def set_nombre(self, nombre):
        self.__nombre == nombre
    
    def get_nombre(self):
        return self.__nombre
    
    def set_telf(self, telf):
        self.__telf == telf
    
    def get_telf(self):
        return self.__telf
    
    def show(self):
        return f"""
        Nombre Motorizado: {self.__nombre}
        Telefono Motorizado: {self.__tefl}
        """