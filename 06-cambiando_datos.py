"""
METODOS

split   -> string a lista (puedes indicarle a partir de que caracter de texto quieres cortar)
join    -> lista a string    

----------------------------------
Exercise 1: cortar un texto y convertirlo en lista con split
name = "Ricardo Garrido Cruz"
nombre_cortado= name.split()
print(nombre_cortado)

-------------------------------------------
Exercise 2: cortar un texto y convertirlo en lista con split pero indicandole donde cortar
NOTA: dejo un espacio después de la "coma" para que no se guarde en la lista con un espacio "al inicio"
texto = "Hola! Mi nombre es Ricardo, vivo en cuernavaca, soy programador, tengo 39 años, estoy casado y soy mexicano."
texto_cortado= texto.split(",")
print(texto_cortado)

----------------------------------------------------
Exercise 3: Convierte una lista a texto y separalo
NOTA: poner las comillas de string antes de la función "join", nos sirve como separador,
le puedes poner una COMA, un ESPACIO o AMBOS y la "lista" dentro de la función

cursos = ["ruby","python","sql","html","css"]
lista = ", ".join(cursos)
print(lista)

-----------------------------------------------------------------
Exercise 4: Concatena un entero y un texto
name= "ric"
numero = 2
concatenar = name + str(numero)
print(concatenar)

--------------------------------------------------------------------------
Exercise 5: Concatena 2 variables usando el metodo "join"


name= "ric"
last_name = "garrido"
concatenar = " ".join([name,last_name])
print(concatenar)

-----------------------------------------------------------------------------
Exercise 6: 

"""
