
class TarjetaCredito:
    def __init__(self, numero_tarjeta, saldo_pendiente):
        self.numero_tarjeta = numero_tarjeta
        self.saldo_pendiente = saldo_pendiente

    @staticmethod
    def validar_tarjeta(numero):
        tarjeta_lista = list(numero)
        tarjeta_lista.reverse()
        tarjeta_int = list(map(int, tarjeta_lista))

        for i in range(1, len(tarjeta_int), 2):
            tarjeta_int[i] *= 2
            if tarjeta_int[i] > 9:
                tarjeta_int[i] -= 9

        suma = sum(tarjeta_int)
        return suma % 10 == 0

    def consultar_saldo_pendiente(self):
        return self.saldo_pendiente

    def pagar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo_pendiente:
            self.saldo_pendiente -= cantidad
            print(f"Pago realizado. Nuevo saldo pendiente: {self.saldo_pendiente}")
        else:
            print("ERROR: Fondos insuficientes o cantidad inválida.")


class CuentaBancaria:
    def __init__(self, saldo, titular, tarjeta):
        self.__saldo = saldo
        self.__titular = titular
        self.tarjeta = tarjeta

    def depositar(self, cantidad):
        if TarjetaCredito.validar_tarjeta(self.tarjeta.numero_tarjeta):
            if cantidad > 0:
                self.__saldo += cantidad
                print(f"Depósito exitoso. Nuevo saldo: {self.__saldo}")
            else:
                print("ERROR: La cantidad debe ser mayor que 0.")
        else:
            print("ERROR: Tarjeta no válida. Operación cancelada.")

    def retirar(self, cantidad):
        if TarjetaCredito.validar_tarjeta(self.tarjeta.numero_tarjeta):
            if cantidad > 0 and cantidad <= self.__saldo:
                self.__saldo -= cantidad
                print(f"Retiro exitoso. Nuevo saldo: {self.__saldo}")
            else:
                print("ERROR: Fondos insuficientes o cantidad inválida.")
        else:
            print("ERROR: Tarjeta no válida. Operación cancelada.")

    def consultar_saldo(self):
        if TarjetaCredito.validar_tarjeta(self.tarjeta.numero_tarjeta):
            print(f"Saldo actual: {self.__saldo}")
        else:
            print("ERROR: Tarjeta no válida.")

    def consultar_titular(self):
        if TarjetaCredito.validar_tarjeta(self.tarjeta.numero_tarjeta):
            print(f"Titular de la cuenta: {self.__titular}")
        else:
            print("ERROR: Tarjeta no válida.")

    def realizar_pago_tarjeta(self, cantidad):
        if TarjetaCredito.validar_tarjeta(self.tarjeta.numero_tarjeta):
            if cantidad > 0 and cantidad <= self.__saldo:
                self.__saldo -= cantidad
                self.tarjeta.pagar(cantidad)
                print(f"Pago de tarjeta realizado. Nuevo saldo de la cuenta: {self.__saldo}")
            else:
                print("ERROR: Fondos insuficientes o cantidad inválida.")
        else:
            print("ERROR: Tarjeta no válida. Operación cancelada.")


# Creación de objetos
tarjeta = TarjetaCredito("4539148803436467", 100000)
cuenta = CuentaBancaria(800000, "Maria", tarjeta)

# Menú interactivo con match-case (switch)
while True:
    print("\n=== MENÚ DE CUENTA BANCARIA ===")
    print("1. Consultar saldo")
    print("2. Consultar titular")
    print("3. Depositar dinero")
    print("4. Retirar dinero")
    print("5. Consultar saldo pendiente de tarjeta")
    print("6. Pagar tarjeta")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            cuenta.consultar_saldo()
        case "2":
            cuenta.consultar_titular()
        case "3":
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cuenta.depositar(cantidad)
        case "4":
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cuenta.retirar(cantidad)
        case "5":
            print(f"Saldo pendiente de la tarjeta: {tarjeta.consultar_saldo_pendiente()}")
        case "6":
            cantidad = float(input("Ingrese la cantidad a pagar: "))
            cuenta.realizar_pago_tarjeta(cantidad)
        case "7":
            print("Saliendo del programa...")
            break
        case _:
            print("Opción inválida. Intente de nuevo.")
