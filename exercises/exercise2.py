"""Variables de Clase y Métodos de Clase."""


from mailbox import NoSuchMailboxError


class Article:
    """Todos los artículos tienen un nombre y un costo, opcionalmente algunos
    tienen un porcentaje de descuento.

    El IVA es un impuesto que se aplica a todos los productos por igual,
    actualmente es de 21% pero puede cambiar en el futuro.

    Para calcular el precio de un artículo, hay que sumar el IVA y luego restar
    los descuentos si hubiera. Redondear a 2 decimales.

    Restricciones:
        - Utilizar 3 variables de instancia
        - Utilizar 1 método de instancia
        - Utilizar 1 variable de clase
        - Utilizar 1 método de clase
        - No utilizar Dataclasses
        - No utilizar Properties
        - Utilizar Type Hints en todos los métodos y variables
    """
    __IVA = 0.21

    def __init__(self, nombre, costo, descuento = 0):
        self.nombre = nombre
        self.costo = costo 
        self.descuento = descuento
    
    def calcular_precio (self):
        precio_iva = round((self.costo * self.__IVA) + self.costo,2)
        precio = round((precio_iva - precio_iva * self.descuento),2)
        return precio

    @classmethod
    def actualizar_iva(cls, iva_nuevo):
        cls.__IVA = iva_nuevo
        return cls.__IVA

# NO MODIFICAR - INICIO
# Test parámetro obligatorio
try:
    article = Article()
    assert False, "No se puede instanciar sin nombre ni costo"
except TypeError:
    assert True

try:
    article = Article("Auto")
    assert False, "No se puede instanciar sin costo"
except TypeError:
    assert True

try:
    article = Article(nombre="Auto", costo=1)
    assert True
except TypeError:
    assert False, "El descuento es opcional"

# Test básico
article = Article("Auto", 1)
assert article.nombre == "Auto"
assert article.calcular_precio() == 1.21

article = Article("Auto", 1, 0.21)
assert article.nombre == "Auto"
assert article.calcular_precio() == 0.96


# Test palabra clave
article = Article(costo=1, nombre="Auto")
assert article.nombre == "Auto"
assert article.calcular_precio() == 1.21

article = Article(costo=1, nombre="Auto", descuento=0.21)
assert article.nombre == "Auto"
assert article.calcular_precio() == 0.96


# Test de método de clase
Article.actualizar_iva(0.25)

article = Article(costo=1, nombre="Auto")
assert article.nombre == "Auto"
assert article.calcular_precio() == 1.25
# NO MODIFICAR - FIN
