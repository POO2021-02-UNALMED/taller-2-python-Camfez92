class Asiento:
    def __init__(self,color,precio,registro):
        self.color=color
        self.precio=precio
        self.registro=registro
    
    def cambiarColor(self,color):
        if color in ['rojo','verde','amarillo','negro','blanco']:
            self.color=color

class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro

    def cambiarRegistro(self,registro):
        self.registro=registro
    
    def asignarTipo(self,tipo):
        if tipo in ['gasolina','electrico']:
            self.tipo=tipo

class Auto:
    cantidadCreados=0
    
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.motor=motor
        self.registro=registro

    def cantidadAsientos(self):
        cantAsientos=0
        for asiento in self.asientos:
            if type(asiento) is Asiento:
                cantAsientos+=1
    
        return cantAsientos

    def verificarIntegridad(self):
        original=True
        if self.motor.registro!=self.registro:
            original=False
                                    
        else:
            for asiento in self.asientos:
                if type(asiento) is Asiento:
                    if asiento.registro!=self.registro:
                        original=False
        
        if original!=True:
            return 'Las piezas no son originales'
        else:
            return 'Auto original'


