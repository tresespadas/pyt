#!/usr/bin/python3

class CuentaBancaria:
    def __init__(self, saldo, titular):
        self._saldo = saldo
        self._titular = titular

    def retirarDinero(self, cantidad):
        if self._saldo < cantidad:
            print(f"Operación no permitida. Saldo inferior a {cantidad}")
        else:
            self._saldo -= cantidad

    def comprobarSaldo(self):
        return f"Dispone de {self._saldo} euros."

cuenta = CuentaBancaria(1000, "Álvaro")
cuenta.retirarDinero(100)
print(cuenta.comprobarSaldo())
