# Se requiere implementar un sistema que gestione información de deudores

# Deudor:

# Dni

# Apellido

# Nombre

# DniCotitular

# ApellidoCotitular

# NombreCotitular

# MontoAdeudado

# AnioDeuda

# Se implantaran varios constructores:

# ·         Un constructor por defecto (sin parámetros).

# ·         Un constructor con todos los atributos como parámetro.

# Al comienzo de la ejecución del programa se solicitará al usuario el ingreso de todos los datos del deudor

# Se deberán implementar las siguientes funciones, que serán accedidas por menú de opciones:

# ·         -CalcularDeudaActual (La deuda actual se calculará teniendo en cuenta el año de la deuda. Por cada año la deuda incrementará un 21%. Por ejemplo, si el monto es $10.000 y el año es 2020, la deuda actual será de $16.300)

# ·         -RealizarPlanDePago (se solicitará el ingreso de las cuotas deseadas.

# Partiendo de la deuda actual, si el plan no excede las 3 cuotas no tendrá interés adicional. De 4 a 6 cuotas se sumará un interes del 10%. De 7 a 12 cuotas se sumará un      interes del 19%. El metodo deberá devolver el valor de cada cuota.)

# ·         -CambiarCotitular (se solicitarán los datos del nuevo cotitular y se incrementará la deuda un 5%)

# ·         -Ver datos personales del deudor

# ·         -Ver datos personales del cotitular

# ·         -Ver todos los datos del deudor
class Deudor:
    def __init__(self,dni="",apellido="",nombre="",dni_cotitular="",apellido_cotitular="",nombre_cotitular="",monto_adeudado="",año_deuda=""):
        self.dni = dni
        self.apellido = apellido
        self.nombre = nombre
        self.dni_cotitular = dni_cotitular
        self.apellido_cotitular = apellido_cotitular
        self.nombre_cotitular = nombre_cotitular
        self.monto_adeudado = float(monto_adeudado)
        self.año_deuda = año_deuda

    def CalcularDeudaActual (self):
        año_actual = 2025
        años = año_actual - self.año_deuda
        deuda_actual = self.monto_adeudado

        contador = 0
        while contador < años:
            deuda_actual = deuda_actual * 1.21
            contador = contador + 1
        
        deuda_actual = int(deuda_actual * 100 + 0.5) / 100
        return deuda_actual
    
    def realizar_plan_de_pago(self, cuotas):
        deuda = self.CalcularDeudaActual()
        intereses = 0
        if cuotas <= 3:
            intereses = 0
        elif cuotas >=4 and cuotas <=6:
            intereses = 0.10
        elif cuotas >=7 and cuotas <=12:
            intereses = 0.19
        else:
            print("Cantidad de cuotas no permitidas.")
            return None
        
        total_con_intereses = deuda * (1 + intereses)
        valor_cuotas = total_con_intereses / cuotas
        valor_cuotas = int(valor_cuotas * 100 + 0.5) /100
        return valor_cuotas
    
    def cambiar_cotitular(self, dni, apellido, nombre):
        self.dni_cotitular = dni
        self.apellido_cotitular = apellido
        self.nombre_cotitular = nombre
        self.monto_adeudado = self.monto_adeudado * 1.05

    def ver_datos_personales(self):
        print("Deudor: " + self.nombre + "" + self.apellido + "- DNI: " + self.dni)

    def ver_datos_cotitular(self):
        self.ver_datos_personales()
        self.ver_datos_cotitular()
        monto_redondeado = int(self.monto_adeudado * 100 + 0.5) / 100
        print("Monto adeudado original: $" + str(monto_redondeado))
        print("Año de deuda: " + str(self.año_deuda))
        print("Deuda actual: $" + str(self.CalcularDeudaActual()))

def menu():
    print("\n---Menú de opciones---")
    print("1- Calcular deuda actual")
    print("2- Realizar plan de pago")
    print("3- Cambiar cotitular")
    print("4- Ver datos personales del deudor")
    print("5- Ver datos personales del cotitular")
    print("6- Ver todos los datos del deudor")
    print("0- Salir")
    return input("Seleccione una opción: ")
def ingresar_datos_deudor():
    print("Ingrese datos del deudor: ")
    dni = input("DNI: ")
    apellido = input("Apellido: ")
    nombre = input("Nombre: ")
    dni_cotitular = input("DNI cotitular: ")
    apellido_cotitular = input("Apellido cotitular: ")
    nombre_cotitular = input("Nombre cotitular: ")
    monto = float(input("Monto adeudado: "))
    año = int(input("Año de la deuda: "))
    return Deudor(dni,apellido,nombre,dni_cotitular,apellido_cotitular,nombre_cotitular, monto, año)

deudor = ingresar_datos_deudor()

ejecutar_menu = True
while ejecutar_menu:
    opcion = menu()
    if opcion == "1":
        print("Deuda actual: $", str(deudor.CalcularDeudaActual()))
    elif opcion == "2":
        cuota = int(input("Ingrese la cantidad de cuotas: "))
        valor = deudor.realizar_plan_de_pago(cuota)
        if valor is not True:
            print("Valor de cada cuota: $", str(valor))
    elif opcion == "3":
        print("Ingrese los nuevos datos del cotitular: ")
        dni = input("DNI cotitular: ")
        apellido = input("Apeliido cotitular: ")
        nombre = input("Nombre cotitular: ")
        deudor.cambiar_cotitular(dni,apellido,nombre)
        print("Cotitular actualizado, Deuda incrementada en 5%")
    elif opcion == "4":
        deudor.ver_datos_personales()
    elif opcion == "5":
        deudor.ver_datos_cotitular()
    elif opcion == "6":
        deudor.ver_todos_los_datos()
    elif opcion == "0":
        print("Gracias, adios")
        ejecutar_menu = False
    else:
        print("Opcion no valida")
        