#El juego se llama "Locas Historias". La intención del juego es colocar palabras para rellenar en una frase y aplicar la operación de concatenación en el tipo de datos STRING. 



# print(f'Aprende a programar con {organiza}')    #Esto se llama f-string
print("*****************************************************************************")
print("   ****************BIENVENIDOS AL JUEGO DE LOCAS HISTORIAS****************   ")
print("*****************************************************************************")
print()
print()
print("La intención del juego es colocar palabras para completar una frase u oración, sabiendo diferenciar cada una de sus partes o elementos.\nA continuación te mostramos la frase, y no te preocupes, no existe una forma correcta, sencillamente se trata de construir una frase con sentido.")
print()
#print()
print('La frase es: \n"Programar es tan ______________!. Siempre emociona, porque encanta ____________. Aprende a _____________ con diferentes ____________ y alcanza tus ____________."')

print()
print()
adjetivo_01=input('Ingresa un adjetivo: ')
verbo_01=input('Ingresa un verbo: ')
verbo_02=input('Ingresa un verbo: ')
sustantivo_01=input('Ingresa un sustantivo (en plural): ')
sustantivo_02=input('Ingresa un sustantivo (en plural): ')


frase = f'Programar es tan {adjetivo_01}!. Siempre emociona, porque encanta {verbo_01}. Aprende a {verbo_02} con diferentes {sustantivo_01} y alcanza tus {sustantivo_02}.'
print()
print(frase)
print()
a=input('Quieres seguir jugando (s/n): ')
print()
while (a=="s") or (a=="S"):
    adjetivo_01=""
    verbo_01=""
    verbo_02=""
    sustantivo_01=""
    sustantivo_02=""
    print()
    print('Programar es tan ______________!. Siempre emociona, porque encanta ____________. Aprende a _____________ con diferentes ____________ y alcanza tus ____________.')
    
    print()
    adjetivo_01=input('Ingresa un adjetivo: ')
    verbo_01=input('Ingresa un verbo: ')
    verbo_02=input('Ingresa un verbo: ')
    sustantivo_01=input('Ingresa un sustantivo (en plural): ')
    sustantivo_02=input('Ingresa un sustantivo (en plural): ')
    print()
    frase = f'Programar es tan {adjetivo_01}!. Siempre emociona, porque encanta {verbo_01}. Aprende a {verbo_02} con diferentes {sustantivo_01} y alcanza tus {sustantivo_02}.'
    print(frase)
    print()
    a=input('Quieres seguir jugando (s/n): ')
    print()
print()
print('***GRACIAS POR PARTICIPAR***')