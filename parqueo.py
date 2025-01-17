class Parqueosali():
    def init(self):
        self.espaciosdisponibles = 25
        self.vehiculos = []
        self.totalrecaudado = 0
        self.contadorautomoviles = 0
        self.contadorbusetas = 0
        self.contadormotos = 0

    def entrada_vehiculo(self):
        if self.espaciosdisponibles == 0:
            print("El parqueo está lleno. No se puede ingresar más vehículos.")
            return

        tipovehiculo = input("Ingrese el tipo de vehículo (automóvil/buseta/moto): ").lower()
        if tipovehiculo not in ['automóvil', 'buseta', 'moto']:
            print("Tipo de vehículo no válido.")
            return

        horaentrada = int(input("Ingrese la hora de entrada (0-23): "))
        if horaentrada < 0 or horaentrada > 23:
            print("Hora de entrada no válida.")
            return

        self.vehiculos.append((tipovehiculo, horaentrada))
        self.espaciosdisponibles -= 1
        print(f"Vehículo ingresado. Espacios disponibles: {self.espaciosdisponibles}")

        if tipovehiculo == 'automóvil':
            self.contadorautomoviles += 1
        elif tipovehiculo == 'buseta':
            self.contadorbusetas += 1
        elif tipovehiculo == 'moto':
            self.contadormotos += 1

    def salida_vehiculo(self):
        if not self.vehiculos:
            print("No hay vehículos en el parqueo.")
            return

        tipovehiculo, horaentrada = self.vehiculos.pop()
        horasalida = int(input("Ingrese la hora de salida (0-23): "))
        if horasalida < 0 or horasalida > 23:
            print("Hora de salida no válida.")
            return

        horasparqueo = horasalida - horaentrada
        if horasparqueo < 0:
            print("La hora de salida no puede ser anterior a la hora de entrada.")
            return

        if tipovehiculo == 'automóvil':
            costo = horasparqueo * 1500
        elif tipovehiculo == 'buseta':
            costo = horasparqueo * 3000
        elif tipovehiculo == 'moto':
            costo = horasparqueo * 1000

        print(f"Vehículo tipo {tipovehiculo} salió. Costo total: {costo} pesos.")
        self.espaciosdisponibles += 1

        if tipovehiculo == 'automóvil':
            self.contaaorautomoviles -= 1
        elif tipovehiculo == 'buseta':
            self.contadorbusetas -= 1
        elif tipovehiculo == 'moto':
            self.contadormotos -= 1

    def estado_parqueo(self):
        print(f"Espacios disponibles: {self.espaciosdisponibles}")
        print(f"Total automóviles: {self.contadorautomoviles}")
        print(f"Total busetas: {self.contadorbusetas}")
        print(f"Total motos: {self.contadormotos}")

# Ejemplo de uso
Parqueo = (10)  # Inicializa el parqueo con 10 espacios
Parqueo.ingresarvehiculo()
Parqueo.salidavehiculo()
Parqueo.estadoparqueo()