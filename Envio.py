import typing

class Envio:
    def __init__(self, orden_compra : str, servicio_envío : str,  motorizado : str, costo_servicio : str, fecha_envio : str):
        self.__orden_compra = orden_compra
        self.__servicio_envio = servicio_envío
        self.__motorizado = motorizado
        self.__costo_servicio = costo_servicio
        self.__fecha_envio = fecha_envio

    def set_fecha_Envio(self, fecha_envio):
        self.__fecha_envio = fecha_envio

    def get_fecha_envio(self):
        return self.__fecha_envio

    def set_orden_compra(self, orden_compra):
        self.__orden_compra = orden_compra

    def get_orden_compra(self):
        return self.__orden_compra
    
    def set_servicio_envio(self, servicio_envio):
        self.__servicio_envio = servicio_envio

    def get_servicio_envio(self):
        return self.__servicio_envio
    
    def set_motorizado(self, motorizado):
        self.__motorizado = motorizado

    def get_motorizado(self):
        return self.__motorizado
    
    def set_costo_servicio(self, costo_servicio):
        self.__costo_servicio = costo_servicio

    def get_costo_servicio(self):
        return self.__costo_servicio
    
    def show(self):
        return f"""
        Orden Compra: {self.__orden_compra}
        Servicio Envio: {self.__servicio_envio}
        Motorizado: {self.__motorizado}
        Costo Servicio: {self.__costo_servicio}
        """