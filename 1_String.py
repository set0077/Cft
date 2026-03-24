"""
Primer Programa modificacion de texto
"""

Texto = ("INsErTar tExtO 2077")
print(Texto.lower())
print(Texto.upper())
print(Texto.find("20"))


lol = (Texto.center(50, "-"))
print(lol.upper())















def divide (a, b):
    retorno = 0
    if (a == 0):
        retorno = -1
    else:
        retorno = (a/b)
    return(retorno)

print (divide(12, 4))