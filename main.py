from Escuderia import Escuderia

escuderias = []
contador = 1
numeroEscuderias = int(input("Digite el numero de escuderias: "))
while contador <= numeroEscuderias:
    escuderia = Escuderia ()
    escuderia.nombreEscuderia = input("Digite el nombre de la escuderia: ")
    escuderia.motor = input("Digite el nombre del motor: ")
    escuderia.pilotoPrincipal = input("Digite el nombre del piloto principal: ")
    escuderia.pilotosSecundario =  input("Digite el nombre del piloto secundario: ")
    escuderia.costos = int(input("Digite el nombre del costo anual de la escuderia: "))
    escuderias.append(escuderia)
    contador = contador + 1


costoMayor = 0
nombreEscuderiaMasCara = None

for escuderia in escuderias:
    if escuderia.costos > costoMayor:
        costoMayor = escuderia.costos
        nombreEscuderiaMasCara = escuderia.nombreEscuderia


print(f'La Escuderia mas cara es:{nombreEscuderiaMasCara} y el costos final es: ${costoMayor} ')
