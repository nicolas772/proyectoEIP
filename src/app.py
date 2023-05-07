import time
import src.logica.logica1 as L1
import src.logica.logica2 as L2
import src.logica.logica3 as L3
def main():
    print('\n','-------- Proyecto EIP: Trotadora Inteligente ------------', '\n')
    active = True
    print('Ingrese el Rango para el sensor de ritmo cardiaco: ', '\n')
    minRange = input('Rango Minimo [lat/min]: ')
    maxRange = input('Rango Maximo [lat/min]: ')
    print(' ')
    while active:   
        print('[1] Representar envío de cola aleatorio')
        print('[2] Representar envio alternado')
        print('[3] Representar envio de señal de cancelacion')
        print('[4] Salir')
        print(' ')
        opcion = input('Ingrese su opción: ')

        if opcion in ['1','2','3','4']:
            if opcion == '1':
                L1.logica1(int(minRange), int(maxRange))
            elif opcion == '2':
                L2.logica2(int(minRange), int(maxRange))
            elif opcion == '3':
                L3.logica3(int(minRange), int(maxRange))
            else:
                active = False
        else:
            print('\n','Ingrese una opcion valida!', '\n')

    print('\n','-------- Hasta Pronto ------------', '\n')
    time.sleep(1)