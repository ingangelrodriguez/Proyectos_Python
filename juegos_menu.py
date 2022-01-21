#ESTE ES UN MENU DE JUEGOS QUE SE EJECUTA, DE ACUERDO A LA OPCION QUE SELECCIONASTE

print()
print("     *****************************************************************************     ")
print("     ***********************BIENVENIDOS AL MENÚ DE JUEGOS*************************     ")
print("     *****************************************************************************     ")
print()
print()
print("ESTE ES UN MENU DE JUEGOS QUE SE EJECUTA, DE ACUERDO A LA OPCIÓN QUE SELECCIONASTE. \nSOLO TRABAJAREMOS CON LOS JUEGOS DESARROLLADOS HASTA AHORA.")
print()
print("El menú es el siguiente: \n(a): 'LOCAS HISTORIAS' \n(b): 'ADIVINA EL NÚMERO'")
print()
print('Esperamos que los juegos sean de tu agrado')
print()
x=input("Selecciona una de los juegos(a/b): ")
print()

if (x=="a"):
    import Locas_Historias
elif (x=="b"):
    import adivina_el_numero    