"""
Ejemplo de Funcion creada
"""


def aritmetica(num1, num2, op):
        """
        Probando los textos dentro de variables
        cualquier cosa nose XD
        """
    
        if op == 1:
            suma = num1 + num2
            print(suma)
            
        elif op == 2:
            resta = num1 - num2
            print(resta)
            
        elif op == 3:
            multiplicacion = num1 * num2
            print(multiplicacion)
           
        elif op == 4:
            retorno = -1
            division = num1 / num2
            if num1 == 0:
                 print(retorno)
            else: 
                print(division)
          
        else:
            print("Ingrese una opcion valida porfavor")
            


texto =("Main proyect")
print(texto.center(50, "-"))
var = int(input("ingrese el primer numero: "))
var2 = int(input("ingrese el segundo numero: "))
var3 =int(input("ingrese una opcion: "))
print("El resultado es:")
aritmetica(var, var2, var3)

