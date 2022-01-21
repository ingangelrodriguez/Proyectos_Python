#ESTE JUEGO SE TRATA DE QUE LA PERSONA ADIVINE UN NUMERO ALEATORIO FIJADO POR LA COMPUTADORA

import random #VAMOS A IMPORTAR ESTE MODULO PARA LA ALEATORIEDAD, Y SEGUIDAMENTE DEFINIMOS UNA FUNCION


print()
print("     *****************************************************************************     ")
print("     ****************BIENVENIDOS AL JUEGO: ADIVINA EL NÚMERO**********************     ")
print("     *****************************************************************************     ")
print()
print()


print("ESTE JUEGO SE TRATA, DE QUE LA PERSONA ADIVINE UN NÚMERO ALEATORIO FIJADO POR LA COMPUTADORA. \nSOLO TRABAJAREMOS CON NÚMEROS ENTEROS POSITIVOS")
print()


def adivina_el_numero(a):
    
    print()
    num_aleat=random.randint(1,a) #ESTO GENERA UN NUMERO ENTRE 1 Y A (INCLUSIVE AMBOS)
    num_jug=0
    b=''
    

    while (num_jug != num_aleat) :
        num_jug=int(input(f"Adivina un número que se encuentre entre 1 y {a}: "))

        if  (num_jug < 1):
            print()
            print("TEN CUIDADO, EL NUMERO QUE COLOCASTE ES MENOR A 1, Y ASI NO FUNCIONA EL JUEGO")
            print()            
        elif (num_jug < num_aleat): 
            print()
            print("Intenta nuevamente, el valor que colocaste es menor al número generado por la computadora")
            print()           
        elif (num_jug > a):
            print()
            print(f"TEN CUIDADO, EL NUMERO QUE COLOCASTE ES MAYOR A {a}, Y ASI NO FUNCIONA EL JUEGO")
            print()
        elif(num_jug > num_aleat): 
            print()
            print("Intenta nuevamente, el valor que colocaste es mayor al número generado por la computadora")
            print()     
        else:    
            print()
            print(f"Excelente!... \nAdivinaste el valor correcto que es: {num_aleat}")
            print()    
            b=input("Quieres jugar nuevamente?(s/n): ")
            if ((b=="s") or (b=="S")):
                print()
                x=int(input("Para iniciar, ingresa un número entero positivo, hasta donde quieras establecer el intervalo de aleatoriedad: "))
                print()
                while (x<=0):
                    print("Intentalo otra vez")
                    print()
                    x=int(input("Para iniciar, ingresa un número entero positivo, hasta donde quieras establecer el intervalo de aleatoriedad: "))  
                adivina_el_numero(x)
            else:
                    print()
                    print("*****GRACIAS POR PARTICIPAR EN ESTE EXPERIMENTO*****")  



x=int(input("Para iniciar, ingresa un número entero positivo, hasta donde quieras establecer el intervalo de aleatoriedad: "))            
             

while (x<=0):
    print("Intentalo otra vez")
    x=int(input("Para iniciar, ingresa un número entero positivo, hasta donde quieras establecer el intervalo de aleatoriedad: "))      
adivina_el_numero(x)      





        

