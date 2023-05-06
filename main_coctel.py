from Coctel import Coctel

cocteles = []
contador = 1
ventaShot = int(input('Cuantos shots se van a vender: '))
getVenta = 1
while getVenta == 1:
    while contador <= ventaShot:
        coctel = Coctel()
        tipo_shot = int(input('Que tipo de SHOT desea ingresar, 1 para shot de frutas o 2 para shot de alchol: '))
        if tipo_shot == 1:
            coctel.nombre = input('Digita el nombre del SHOT: ')
            coctel.precio = int(input('Digita el precio del SHOT: '))
            coctel.tipo_coctel = 'SHOT DE FRUTAS'
            coctel.frescura = int(input('Digita los dias de frescuera de las frutas: '))
            coctel.temperatura = None
        elif tipo_shot == 2:
            coctel.nombre = input('Digita el nombre del SHOT: ')
            coctel.precio = int(input('Digita el precio del SHOT: '))
            coctel.tipo_coctel = 'SHOT DE ALCOHOL'
            coctel.frescura = None
            coctel.temperatura = input('Digita la temperatura del SHOT: ')
        else:
            print('Tipo de SHOT no existe')
            break

        cocteles.append(coctel)
        contador = contador + 1

    getVenta = int(input('Desea ingresar una nueva venta? 1 para SI, 2 para NO: '))

costoShotAlcohol = 0
costoShotFruta = 0
cantShotAlcohol = 0
cantShotFruta = 0
shotAlcohol = 'SHOT DE ALCOHOL'
shotFruta = 'SHOT DE FRUTAS'
shotNoSale = 0

for coctel in cocteles:
    if coctel.tipo_coctel == shotAlcohol:
        costoShotAlcohol = costoShotAlcohol + coctel.precio
        cantShotAlcohol = cantShotAlcohol + 1
    elif coctel.tipo_coctel == shotFruta:
        if coctel.frescura == 1:
            costoShotFruta = costoShotFruta + coctel.precio
            cantShotFruta = cantShotFruta + 1
        elif coctel.frescura == 2:
            costoShotFruta = costoShotFruta + (coctel.precio-(coctel.precio*0.2))
            cantShotFruta = cantShotFruta + 1
        elif coctel.frescura == 3:
            costoShotFruta = costoShotFruta + (coctel.precio-(coctel.precio*0.5))
            cantShotFruta = cantShotFruta + 1
        else:
            shotNoSale = shotNoSale + 1


print(f'La canticada de SHOTs de Alcohol vendidos fueron {cantShotAlcohol} y el costo fue {costoShotAlcohol}')
print(f'La canticada de SHOTs de Frutas vendidos fueron {cantShotFruta} y el costo fue {costoShotFruta}')
print(f'La canticada de SHOTs No vendidos fueron {shotNoSale}')



