'''Los tramos impositivos para la declaración de la renta en un determinado país son
los siguientes:

Renta                         Tipo impositivo
Menos de 10000€                     5%
Entre 10000€ y 20000€               15%
Entre 20000€ y 35000€               20%
Entre 35000€ y 60000€               30%
Más de 60000€                       45%

Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla
el tipo impositivo que le corresponde.'''

renta_anual = input("¿Cuanto tienes de renta anual?")
renta_anual = int(renta_anual)

if renta_anual < 10000:
    print('Te corresponde un 5%')
elif renta_anual >= 10000 and renta_anual < 20000:
    print('Te corresponde un 15%')
elif renta_anual >= 20000 and renta_anual < 35000:
    print('Te corresponde un 20%')
elif renta_anual >= 35000 and renta_anual < 60000:
    print('Te corresponde un 30%')
else:
    print('Te corresponde un 45%')
