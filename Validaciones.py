import re

class Validaciones:
    
    def validar_fecha(self, teclado):
        patron = r'^\d{2}/\d{2}/\d{4}$'
        if re.match(patron, teclado):
            return True
        else:
            return False
        
    def validar_entero(self, teclado):
        try:
            valor = int(input(teclado))
            return valor
        except ValueError:
            print("ERROR: INTENTE NUEVAMENTE.")
            return None

    def validar_flotante(self, teclado):
        try:
            valor = float(input(teclado))
            return valor
        except ValueError:
            print("ERROR: INTENTE NUEVAMENTE.")
            return None

    def validar_alfabetico(self, teclado):
        while True:
            ingreso = input(teclado)
            if ingreso.replace(" ", "").isalpha():
                return ingreso
            else:
                print("ERROR: INTENTE NUEVAMENTE.")
        