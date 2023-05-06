class Coctel:
    def __init__(self):
        self.__nombre = None
        self.__precio = None
        self.__tipo_coctel = None
        self.__frescura = None
        self.__temperatura = None

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, dato):
        self.__nombre = dato

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, dato):
        self.__precio = dato

    @property
    def tipo_coctel(self):
        return self.__tipo_coctel

    @tipo_coctel.setter
    def tipo_coctel(self, dato):
        self.__tipo_coctel = dato

    @property
    def frescura(self):
        return self.__frescura

    @frescura.setter
    def frescura(self, dato):
        self.__frescura = dato

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, dato):
        self.__temperatura = dato