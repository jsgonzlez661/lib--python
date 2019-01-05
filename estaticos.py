class Prueba:
    prop1 = "mi propiedad"
    prop2 = "propiedad 2"
    
    @staticmethod
    def set_prop1(valor):
        Prueba.prop1 = valor

    @staticmethod
    def set_prop2(valor):
        Prueba.prop2 = valor

    @staticmethod
    def get_prop1():
        return Prueba.prop1

    @staticmethod
    def get_prop2():
        return Prueba.prop2

    def set_prop1_obj(self, valor):
        self.prop1 = valor 

    def get_prop1_obj(self):
        return self.prop1

obj = Prueba()

obj.set_prop1_obj("cambiada desde objeto")

Prueba.set_prop1("cambiado desde clase")

print("propiedad estática prop1: ", obj.get_prop1_obj())
print("propiedad estática prop1: ", obj.get_prop1())
