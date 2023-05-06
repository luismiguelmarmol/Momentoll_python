class  Escuderia:
    def __init__(self):
        self.__nombreEscuderia =None
        self.__motor = None
        self.__pilotoPrincipal = None
        self.__pilotosSecundario = None
        self.__costos =  None

@property
def nombreEscuderia(self):
    return self.nombreEscuderia

@nombreEscuderia.setter
def nombreEscuderia(self,dato):
        self.__nombreEscuderia = dato

@property
def motor(self):
    return self.motor

@motor .setter
def motor(self,dato):
        self.__motor = dato

@property
def pilotoPrincipal(self):
    return self.pilotoPrincipal

@pilotoPrincipal.setter
def pilotoPrincipal(self,dato):
        self.__pilotoPrincipal = dato

@property
def pilotosSecundario(self):
    return self.__pilotosSecundario

@pilotosSecundario.setter
def pilotosSecundario(self,dato):
        self.__pilotosSecundario = dato

@property
def costos(self):
    return self.__costos

@costos.setter
def costos(self,dato):
        self.__costos = dato