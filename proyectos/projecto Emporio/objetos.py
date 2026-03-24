class Articulo:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre  
        self.precio = precio
        self.stock = stock

"""
Vende librosm revistas, afiches, calendarios, posters
los guardan fisicamente en vitrinas, estantesm Repisa
"""

libro = Articulo("Libro", 3000, 10)
revista = Articulo("revista", 2000, 20)
afiches = Articulo("afiche", 1000, 30)
calendario = Articulo("calendario", 500, 100)
poster = Articulo("poster", 500, 100)

print(libro.nombre, libro.stock)
