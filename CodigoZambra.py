import random

# Inicializar variables
encuestas = []
hombre_total = 0
hombre_trabaja_total = 0
mujer_total = 0
mujer_trabaja_total = 0
hombre_sueldo_total = 0
mujer_sueldo_total = 0

def generar_registros():
    global encuestas
    encuestas = []
    for i in range(10):
        sexo = random.randint(1, 2)
        trabaja = random.randint(1, 2)
        if trabaja == 1:
            sueldo = random.randint(600, 2000)
        else:
            sueldo = 0
        encuestas.append((sexo, trabaja, sueldo))

def calcular_estadisticas():
    global hombre_total, hombre_trabaja_total, mujer_total, mujer_trabaja_total, hombre_sueldo_total, mujer_sueldo_total
    hombre_total = 0
    hombre_trabaja_total = 0
    mujer_total = 0
    mujer_trabaja_total = 0
    hombre_sueldo_total = 0
    mujer_sueldo_total = 0
    for encuesta in encuestas:
        sexo, trabaja, sueldo = encuesta
        if sexo == 1:
            hombre_total += 1
            if trabaja == 1:
                hombre_trabaja_total += 1
                hombre_sueldo_total += sueldo
        else:
            mujer_total += 1
            if trabaja == 1:
                mujer_trabaja_total += 1
                mujer_sueldo_total += sueldo

def mostrar_estadisticas():
    if not encuestas:
        print("No hay registros generados. Por favor, genere registros aleatorios primero.")
        return
    calcular_estadisticas()
    hombre_porcentaje = hombre_total / 10 * 100
    mujer_porcentaje = mujer_total / 10 * 100
    hombre_trabaja_porcentaje = hombre_trabaja_total / hombre_total * 100
    mujer_trabaja_porcentaje = mujer_trabaja_total / mujer_total * 100
    hombre_sueldo_promedio = hombre_sueldo_total / hombre_trabaja_total if hombre_trabaja_total!= 0 else 0
    mujer_sueldo_promedio = mujer_sueldo_total / mujer_trabaja_total if mujer_trabaja_total!= 0 else 0
    print(f"Porcentaje de hombres: {hombre_porcentaje:.2f}%")
    print(f"Porcentaje de mujeres: {mujer_porcentaje:.2f}%")
    print(f"Porcentaje de hombres que trabajan: {hombre_trabaja_porcentaje:.2f}%")
    print(f"Porcentaje de mujeres que trabajan: {mujer_trabaja_porcentaje:.2f}%")
    print(f"Sueldo promedio de hombres que trabajan: {hombre_sueldo_promedio:.2f}")
    print(f"Sueldo promedio de mujeres que trabajan: {mujer_sueldo_promedio:.2f}")


def mostrar_estadisticasB():
    if not encuestas:
        print("No hay registros generados. Por favor, genere registros aleatorios primero.")
        return
    calcular_estadisticas()
    hombre_porcentaje = hombre_total / 10 * 100
    print(f"Porcentaje de hombres: {hombre_porcentaje:.2f}%")


def mostrar_estadisticasC():
    if not encuestas:
        print("No hay registros generados. Por favor, genere registros aleatorios primero.")
        return
    calcular_estadisticas()
    mujer_porcentaje = mujer_total / 10 * 100
    print(f"Porcentaje de mujeres: {mujer_porcentaje:.2f}%")
    
def mostrar_estadisticasD():
    if not encuestas:
        print("No hay registros generados. Por favor, genere registros aleatorios primero.")
        return
    calcular_estadisticas()
    hombre_trabaja_porcentaje = hombre_trabaja_total / hombre_total * 100
    print(f"Porcentaje de hombres que trabajan: {hombre_trabaja_porcentaje:.2f}%")
    
def mostrar_estadisticasE():
    if not encuestas:
        print("No hay registros generados. Por favor, genere registros aleatorios primero.")
        return
    calcular_estadisticas()
    mujer_trabaja_porcentaje = mujer_trabaja_total / mujer_total * 100
    print(f"Porcentaje de mujeres que trabajan: {mujer_trabaja_porcentaje:.2f}%")
    
def mostrar_estadisticasF():
    if not encuestas:
        print("No hay registros generados. Por favor, genere registros aleatorios primero.")
        return
    calcular_estadisticas()
    hombre_sueldo_promedio = hombre_sueldo_total / hombre_trabaja_total if hombre_trabaja_total!= 0 else 0
    print(f"Sueldo promedio de hombres que trabajan: {hombre_sueldo_promedio:.2f}")
    
def mostrar_estadisticasG():
    if not encuestas:
        print("No hay registros generados. Por favor, genere registros aleatorios primero.")
        return
    calcular_estadisticas()
    mujer_sueldo_promedio = mujer_sueldo_total / mujer_trabaja_total if mujer_trabaja_total!= 0 else 0
    print(f"Sueldo promedio de mujeres que trabajan: {mujer_sueldo_promedio:.2f}")



def main():
    while True:
        print("Menu:")
        print("a) Generar registros aleatorios")
        print("b) Porcentaje de hombres (tengan o no trabajo).")
        print("c) Porcentaje de mujeres (tengan o no trabajo).")
        print("d) Porcentaje de hombres que trabajan.")
        print("e) Porcentaje de mujeres que trabajan.")
        print("f) El sueldo promedio de los hombres que trabajan.")
        print("g) El sueldo promedio de las mujeres que trabajan.")
        print("h) Mostrar todas las estadisticas.")
        print("i) Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "a":
            generar_registros()
            print("Registros generados con éxito.")
        elif opcion == "b":
            mostrar_estadisticasB()
            
        elif opcion == "c":
            mostrar_estadisticasC()
        elif opcion == "d":
            mostrar_estadisticasD()
        elif opcion == "e":
            mostrar_estadisticasE()
        elif opcion == "f":
            mostrar_estadisticasF()
        elif opcion == "g":
            mostrar_estadisticasG()
        elif opcion == "h":
            mostrar_estadisticas()
        elif opcion == "i":
            print("Adiós!")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()