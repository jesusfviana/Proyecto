import  typing

class Producto:
    def __init__(self, nombre : str, descripcion : str, precio : float, categoria : str, inventario_disponible : int):
        self.nombre = nombre
        self.__descripcion = descripcion
        self.__precio = precio
        self.__categoria = categoria
        self.__inventario_disponible = inventario_disponible

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre
    
    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def get_descripcion(self):
        return self.__descripcion
    
    def set_precio(self, precio):
        self.__precio = precio

    def get_precio(self):
        return self.__precio
    
    def set_categoria(self, categoria):
        self.__categoria = categoria

    def get_categoria(self):
        return self.__categoria
    
    def set_inventario_disponible(self, inventario_disponible):
        self.__inventario_disponible = inventario_disponible

    def get_inventario_disponible(self):
        return self.__inventario_disponible
    
    def show(self):
        return f"""
        Nombre: {self.nombre}
        Descripcion: {self.__descripcion}
        Precio: ${self.__precio}
        Categoria: {self.__categoria}
        Inventario Disponible: {self.__inventario_disponible} unidades disponibles
        """